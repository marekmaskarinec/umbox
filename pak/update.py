
import os
import io
import json
import zipfile

import common


versions = {}


def mkdir(path):
    if not os.path.isdir(path):
        os.mkdir(path)


def link(src, dst):
    if not os.path.islink(dst):
        os.symlink(src, dst, target_is_directory=True)


def fetch_dep(dep):
    global versions

    print(f"Downloading {dep}...")

    # create pak/dep directory
    mkdir(os.path.join("pak", dep))

    # fetch pak.json and data.zip into pak/dep
    pakjson = common.download(dep, 'pak.json')
    with open(os.path.join("pak", dep, "pak.json"), 'w') as f:
        f.write(pakjson.decode('utf-8'))

    data = common.download(dep, 'pak.zip')
    with zipfile.ZipFile(io.BytesIO(data)) as zf:
        zf.extractall(os.path.join("pak", dep))

    # recursively fetch dependencies, with path set to pak/dep/pak
    deps = json.loads(pakjson)['dependencies']
    fetch_deps(deps)

    # create symlinks in pak/dep/pak to pak/dep
    mkdir(os.path.join("pak", dep, "pak"))
    for d in deps:
        link(os.path.join("..", "..", d), os.path.join("pak", dep, "pak", d))

    versions[dep] = common.download(dep, 'version').decode('utf-8')


def fetch_deps(deps):
    global versions

    if not os.path.isdir("pak"):
        os.mkdir("pak")

    for dep in deps:
        if not os.path.isdir(f"pak/{dep}"):
            fetch_dep(dep)
            continue

        if dep not in versions:
            fetch_dep(dep)
            continue

        if versions[dep] != common.download(dep, 'version').decode('utf-8'):
            fetch_dep(dep)
            continue


def update(args):
    global versions
    meta = common.get_meta()

    try:
        with open('pak/versions.json', 'r') as f:
            versions = json.loads(f.read())
    except:
        pass

    fetch_deps(meta['dependencies'])

    with open('pak/versions.json', 'w') as f:
        f.write(json.dumps(versions))
