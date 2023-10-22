
import argparse

from pak import common
from pak import update


def remove(args):
    par = argparse.ArgumentParser(
        prog="pak remove", description="Remove a package")
    par.add_argument('package', help="package name", action="store")

    ns = par.parse_args(args)

    meta = common.get_meta()

    if ns.package not in meta['dependencies']:
        print("Package not installed")
        return

    meta['dependencies'].remove(ns.package)

    common.set_meta(meta)

    update.update([])
