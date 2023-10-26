
import os

from pak import common


def run(args):
    meta = common.get_meta()

    cmd = meta.get('run')

    if os.name == 'posix' and 'run_posix' in meta:
        cmd = meta.get('run_posix')

    if os.name == 'nt' and 'run_windows' in meta:
        cmd = meta.get('run_windows')

    cmd = cmd.split(' ') + args
    try:
        os.execvp(cmd[0], cmd)
    except Exception as e:
        print(e)
        exit(1)
