
import subprocess
import os
import zipfile

import common


def build(args):
    meta = common.get_meta()

    if 'pre_build' in meta:
        for cmd in meta['pre_build']:
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
