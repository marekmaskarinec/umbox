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

    match ns.mode:
        case 'init':
            init.init(args)
        case 'search':
            search.search(args)
        case 'install':
            install.install(args)
        case 'remove':
            remove.remove(args)
        case 'update':
            update.update(args)
        case 'upload':
            upload.upload(args)
        case 'build':
            build.build(args)
        case 'run':
            run.run(args)
        case 'register':
            register.register(args)
