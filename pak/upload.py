
import argparse
import os
import requests

import common


def upload(args):
    par = argparse.ArgumentParser(
        prog="pak upload", description="Upload a package to the repository")

    par.add_argument('-t', '--token', help="repository token",
                     required=True, action="store")
    par.add_argument('file', help="package file", action="store")
    par.add_argument('-u', '--url', help="pak url",
                     action="store", default=common.url)

    ns = par.parse_args(args)

    if not os.path.isfile(ns.file):
        print("File not found")
        return

    meta = common.get_meta()

    resp = requests.post(f"{ns.url}api/package/{meta['name']}/{ns.token}/upload/{ns.file}",
                         data=open(ns.file, "rb"))

    if not resp.ok:
        print(resp.text)
        exit(1)
