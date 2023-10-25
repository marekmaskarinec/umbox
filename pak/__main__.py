#!/usr/bin/env python

import argparse

from pak import build
from pak import init
from pak import install
from pak import remove
from pak import search
from pak import update
from pak import upload
from pak import run
from pak import register
from pak import common

if __name__ == "__main__":
    par = argparse.ArgumentParser(prog="pak", description="A simple package manager for Umka",
                                  epilog="For more information, visit https://sr.ht/~mrms/pak")

    modes = [
        "build",
        "init",
        "install",
        "remove",
        "run",
        "search",
        "update",
        "upload",
        "register"
    ]

    par.add_argument('-u', '--url', help="pak server url",
                     default="https://pak.tophat2d.dev/", action="store")
    par.add_argument("mode", choices=modes, help="pak mode")

    ns, args = par.parse_known_args()

    common.url = ns.url

    if ns.mode == 'init':
        init.init(args)
    elif ns.mode == 'search':
        search.search(args)
    elif ns.mode == 'install':
        install.install(args)
    elif ns.mode == 'remove':
        remove.remove(args)
    elif ns.mode == 'update':
        update.update(args)
    elif ns.mode == 'upload':
        upload.upload(args)
    elif ns.mode == 'build':
        build.build(args)
    elif ns.mode == 'run':
        run.run(args)
    elif ns.mode == 'register':
        register.register(args)
