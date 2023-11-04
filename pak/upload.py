
import argparse
import os
import requests
import hashlib

from pak import common


def upload(args):
    par = argparse.ArgumentParser(
        prog="pak upload", description="Upload a package to the repository")

    par.add_argument('-t', '--token', help="repository token",
                     required=True, action="store")
    par.add_argument('file', help="package file", action="store")
    par.add_argument('-u', '--url', help="pak url",
                     action="store", default=common.url)

    ns = par.parse_args(args)

    if len(token) == 40:
        print("You seem to have registered an old token.")
    if len(token) != 64:
        print("Invalid token")

    if not os.path.isfile(ns.file):
        print("File not found")
        exit(1)

    meta = common.get_meta()

    token = hashlib.blake2b(ns.token.encode(encoding='utf-8')).hexdigest()

    resp = requests.post(f"{ns.url}api/package/{meta['name']}/{token}/upload/{ns.file}",
                         data=open(ns.file, "rb"))

    if not resp.ok:
        print(resp.text)
        exit(1)
