
import requests

import json
import os

url = "http://localhost:8080/"


def get_meta() -> dict:
    try:
        with open("pak.json", 'r') as f:
            return json.load(f)
    except:
        print("Not in a pak directory")
        exit(1)


def download(package, file) -> bytearray:
    resp = requests.get(f"{url}package/{package}/download/{file}")
    if resp.ok:
        return resp.content
    else:
        print(resp.text)
        exit(1)
