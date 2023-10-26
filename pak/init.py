
import argparse
import os
import re

from . import update

presets = {
    'umka': {
        'mainmod': """fn main() {
    printf("Hello, world!\\n")
}
    """,
        'pakjson': """{{
    "name": "{name}",
    "version": "v0.1.0",
    "author": "{author}",
    "license": "{license}",
    "description": "{description}",
    "readme": "{readme}",
    "link": "{link}",
    "dependencies": ["umka"],
    "include": ["{name}.um"],
    "run_posix": "./pak/umka/linux/umka {name}.um",
    "run_windows": ".\\\\pak\\\\umka\\\\windows\\\\umka.exe {name}.um"
}}
"""
    },
    "tophat": {
        "mainmod": """import (
    "canvas.um"
    "window.um"
    "th.um"
) 

fn init*() {
    window.setup("Hello, world!", 640, 480)
    
    window.onFrame.register({
        canvas.drawText("Hello, world!", { 1, 1 }, th.black, 4)
    })
}
""",
        'pakjson': """{{
    "name": "{name}",
    "version": "v0.1.0",
    "author": "{author}",
    "license": "{license}",
    "description": "{description}",
    "readme": "{readme}",
    "link": "{link}",
    "dependencies": ["tophat"],
    "include": ["pak/tophat/tophat", "pak/tophat/tophat.exe", "{name}.um"],
    "run_posix": "./pak/tophat/tophat -main {name}.um",
    "run_windows": "./pak\\tophat\\tophat.exe -main {name}.um"
}}
"""
    }
}


def validate_name(name: str) -> bool:
    pat = re.compile(r'^[a-z][a-z0-9_]*$')
    return pat.match(name)


def init(args):
    par = argparse.ArgumentParser(
        prog="pak init", description="Initialize a new package")

    par.add_argument('preset', choices=presets.keys(),
                     help="package preset", action="store")
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
    par.add_argument('-r', '--readme', help="package readme",
                     action="store", default="README.md")

    ns = par.parse_args(args)

    if not validate_name(ns.name):
        print("Invalid package name")
        return

    with open(f"{ns.name}.um", "w") as f:
        f.write(presets[ns.preset]['mainmod'])

    with open("pak.json", "w") as f:
        f.write(presets[ns.preset]['pakjson'].format(name=ns.name, author=ns.author, license=ns.license,
                                                     description=ns.description, readme=ns.readme, link=ns.link))

    try:
        os.mkdir("pak")
    except FileExistsError:
        pass

    if os.path.isdir(".git"):
        with open(".gitignore", "a") as f:
            f.write("pak/\n")
            f.write("pak.zip\n")

    if not os.path.isfile(ns.readme):
        with open(ns.readme, "w") as f:
            f.write(
                f"# {ns.name}\n\n{ns.description}\n\n## license\n\n{ns.license}\n")

    update.update([])
