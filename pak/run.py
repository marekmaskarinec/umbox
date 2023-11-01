
import os

from pak import common


def run(args):
    meta = common.get_meta()

    cmd = meta.get('run')

    path_sep = ''

    if os.name == 'posix' and 'run_posix' in meta:
        cmd = meta.get('run_posix')
        path_sep = ':'

    if os.name == 'nt' and 'run_windows' in meta:
        cmd = meta.get('run_windows')
        path_sep = ';'
        
    path = os.environ['PATH']
    deps = meta.get('dependencies')
    for dep in deps:
        path = os.getcwd() + '/pak/' + dep + path_sep + path
    os.environ['PATH'] = path 

    cmd = cmd.split(' ') + args
    try:
        os.execvp(cmd[0], cmd)
    except Exception as e:
        print(e)
        exit(1)
