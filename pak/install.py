
import argparse

import common
import update


def install(args):
    par = argparse.ArgumentParser(
        prog="pak install", description="Install a package")
    par.add_argument('package', help="package name", action="store")

    ns = par.parse_args(args)

    meta = common.get_meta()

    if ns.package in meta['dependencies']:
        print("Package already installed")
        return

    if not common.exists(ns.package):
        print("Package not found")
        return

    meta['dependencies'].append(ns.package)

    common.set_meta(meta)

    update.update('')
