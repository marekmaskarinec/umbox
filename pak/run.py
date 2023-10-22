
import os

import common


def run(args):
    meta = common.get_meta()

    cmd = meta.get('run')

    if os.name == 'posix' and 'run_posix' in meta:
        cmd = meta.get('run_posix')

    if os.name == 'windows' and 'run_windows' in meta:
        cmd = meta.get('run_windows')

    cmd = cmd.split(' ') + args
    os.execlp(cmd[0], cmd[0], ' '.join(cmd[1:]))
