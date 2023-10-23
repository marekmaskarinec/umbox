
import subprocess
import os
import tarfile

from pak import common


def build(args):
    meta = common.get_meta()

    if 'pre_build' in meta:
        code = subprocess.run(meta['pre_build'].split(' '),
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

    with tarfile.TarFile('pak.tar', 'w') as tf:
        for f in files:
            tf.add(f)

    if 'post_build' in meta:
        code = subprocess.run(meta['post_build'].split(' '),
                              stdout=os.sys.stdout, stderr=os.sys.stderr, stdin=os.sys.stdin).returncode

        if code != 0:
            print("Post-build failed")
            exit(code)
