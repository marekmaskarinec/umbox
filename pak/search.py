
import argparse
import requests

from pak import common


def search(args):
    par = argparse.ArgumentParser(
        prog='search', description='Search for a package')
    par.add_argument('query', help='Query string')

    ns = par.parse_args(args)

    resp = requests.get(f"{common.url}api/search/{ns.query}")
    # decode the result from json
    result = resp.json()

    for r in result:
        print(f"{r.get('name')} - {r.get('description')}")
