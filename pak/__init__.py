#!/usr/bin/env python

import argparse

import build
import init
import install
import remove
import search
import update
import upload
import run

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
    ]

    par.add_argument("mode", choices=modes, help="pak mode")

    ns, args = par.parse_known_args()

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
