#!/usr/bin/python3
'''sends a request to a given url and display body.'''

import sys
import requests

if __name__ = "__main__":
    url = sys.agv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.sratus_code))
    else:
        print(r.text)
