
import subprocess
import os
import zipfile

import common


def build(args):
    meta = common.get_meta()

    pre_build = []
    pre_build.append([m['pre_build'] for m in [common.get_meta_of(d)
                     for d in meta['dependencies']] if 'pre_build' in m])
    if 'pre_build' in meta:
        pre_build.append(meta['pre_build'])

    post_build = []
    post_build.append([m['post_build'] for m in [common.get_meta_of(d)
                                                 for d in meta['dependencies']] if 'post_build' in m])
    if 'post_build' in meta:
        post_build.append(meta['post_build'])

    for cmd in pre_build:
        code = subprocess.run(cmd.split(' '),
                              stdout=os.sys.stdout, stderr=os.sys.stderr, stdin=os.sys.stdin).returncode

        if code != 0:
            print("Pre-build failed")
            exit(code)

    files = ['pak.json']
    if 'readme' in meta:
        files.append(meta['readme'])

    for f in meta['include']:
        if os.path.isfile(f):
            files.append(f)
        else:
            for root, dirs, fs in os.walk(f):
                for f in fs:
                    files.append(os.path.join(root, f))

    with zipfile.ZipFile("pak.zip", 'w') as zf:
        for f in files:
            zf.write(f, f, zipfile.ZIP_DEFLATED, compresslevel=9)

    for cmd in post_build:
        code = subprocess.run(cmd.split(' '),
                              stdout=os.sys.stdout, stderr=os.sys.stderr, stdin=os.sys.stdin).returncode

        if code != 0:
            print("Post-build failed")
            exit(code)
