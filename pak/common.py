
import requests

import json
import os

url = "https://pak.tophat2d.dev/"


def get_meta() -> dict:
    try:
        with open("pak.json", 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Not in a pak directory")
        exit(1)
    except:
        print("Could not load pak.json")
        exit(1)


def get_meta_of(name) -> dict:
    with open(f"pak/{name}/pak.json", 'r') as f:
        return json.load(f)


def set_meta(meta: dict):
    with open("pak.json", 'w') as f:
        json.dump(meta, f, indent=4)


def exists(package) -> bool:
    resp = requests.get(f"{url}api/package/{package}/download/version")
    return resp.ok


def download(package, file) -> bytearray:
    resp = requests.get(f"{url}api/package/{package}/download/{file}")
    if resp.ok:
        return resp.content
    else:
        print(resp.text)
        exit(1)
