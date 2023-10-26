
import os
import io
import json
import tarfile
import shutil

from pak import common


versions = {}
touched = set()


def mkdir(path):
    if not os.path.isdir(path):
        os.mkdir(path)


def link(src, dst):
    if not os.path.islink(dst):
        os.symlink(src, dst, target_is_directory=True)


def fetch_dep(dep):
    global versions

    print(f"Downloading {dep}...")

    if not common.exists(dep):
        print(f"Package {dep} not found")
        exit(1)

    # create pak/dep directory
    mkdir(os.path.join("pak", dep))

    # fetch pak.json and data.zip into pak/dep
    pakjson = common.download(dep, 'pak.json')
    with open(os.path.join("pak", dep, "pak.json"), 'w', encoding='utf-8') as f:
        f.write(pakjson.decode(encoding='utf-8', errors='replace'))

    with open("pak/tmp.tar", "wb") as f:
        f.write(common.download(dep, 'pak.tar'))
    with tarfile.TarFile("pak/tmp.tar") as tf:
        tf.extractall(os.path.join("pak", dep))
    os.remove("pak/tmp.tar")

    # recursively fetch dependencies, with path set to pak/dep/pak
    deps = json.loads(pakjson)['dependencies']
    fetch_deps(deps)

    # create symlinks in pak/dep/pak to pak/dep
    mkdir(os.path.join("pak", dep, "pak"))
    for d in deps:
        link(os.path.join("..", "..", d), os.path.join("pak", dep, "pak", d))

    versions[dep] = common.download(dep, 'version').decode(
        encoding='utf-8', errors='replace')


def fetch_deps(deps):
    global versions

    for dep in deps:
        touched.add(dep)

        if not os.path.isdir(f"pak/{dep}"):
            fetch_dep(dep)
            continue

        if dep not in versions:
            fetch_dep(dep)
            continue

        if versions[dep] != common.download(dep, 'version').decode(encoding='utf-8'):
            fetch_dep(dep)
            continue

        # in case a dependency nor it's parent was updated, we still need to touch it
        with open(f"pak/{dep}/pak.json", 'r') as f:
            meta = json.loads(f.read())

        for d in meta['dependencies']:
            touched.add(d)


def update(args):
    global versions
    meta = common.get_meta()

    mkdir("pak")

    try:
        with open('pak/versions.json', 'r') as f:
            versions = json.loads(f.read())
    except:
        pass

    fetch_deps(meta['dependencies'])

    for d in os.listdir('pak'):
        if d == 'versions.json':
            continue

        if not d in touched:
            print(f"Removing {d}...")
            shutil.rmtree(f'pak/{d}')
            del versions[d]

    with open('pak/versions.json', 'w') as f:
        f.write(json.dumps(versions))
