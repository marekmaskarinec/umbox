
import json
import os

url = "http://localhost:8080/"


def get_meta() -> dict:
    try:
        with open("pak.json", 'r') as f:
            return json.load(f)
    except:
        print("Not in a pak directory")
        os.exit(1)
