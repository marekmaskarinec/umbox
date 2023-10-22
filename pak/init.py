
import argparse
import os
import re

mainmod = """fn main() {
    printf("Hello, world!\\n")
}
"""

pakjson = """{{
    "name": "{name}",
    "version": "v0.1.0",
    "author": "{author}",
    "license": "{license}",
    "description": "{description}",
    "link": "{link}",
    "dependencies": [],
    "include": ["{name}.um"],
    "build": []
}}
"""


def validate_name(name: str) -> bool:
    pat = re.compile(r'^[a-z][a-z0-9_]*$')
    return pat.match(name)


def init(args):
    par = argparse.ArgumentParser(
        prog="pak init", description="Initialize a new package")

    par.add_argument('-n', '--name', help="package name",
                     action="store", default=os.path.basename(os.getcwd()))
    par.add_argument('-a', '--author', help="package author",
                     action="store", default=os.environ['USER'])
    par.add_argument('-l', '--license', help="package license",
                     action="store", default="MIT")
    par.add_argument('-d', '--description',
                     help="package description", action="store", default="")
    par.add_argument('-u', '--link', help="package link",
                     action="store", default="")

    ns = par.parse_args(args)

    if not validate_name(ns.name):
        print("Invalid package name")
        return

    with open(f"{ns.name}.um", "w") as f:
        f.write(mainmod)

    with open("pak.json", "w") as f:
        f.write(pakjson.format(name=ns.name, author=ns.author, license=ns.license,
                               description=ns.description, link=ns.link))

    try:
        os.mkdir("pak")
    except FileExistsError:
        pass

    if os.path.isdir(".git"):
        with os.open(".gitignore", "a") as f:
            f.write("pak/\n")
            f.write("pak.zip\n")
