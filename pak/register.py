
import argparse
import requests

import common


def register(args):
    par = argparse.ArgumentParser(
        prog='register', description='Register a package')
    par.add_argument('name', help='Package name')

    ns = par.parse_args(args)

    print(requests.get(f"{common.url}api/register/{ns.name}").text)
