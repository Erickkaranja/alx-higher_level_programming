#!/usr/bin/python3
'''Write a Python script that takes in a letter and sends a POST request .'''

import requests
import sys

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        req = r.json()
        if req == {}:
            print("No result")
        else:
            print("[{}] {}".format(req.get("id"), req.get("name")))
    except ValueError:
        print("Not a valid JSON")
