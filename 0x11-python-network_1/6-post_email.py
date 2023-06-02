#!/usr/bin/python3
'''sends a post request to a given url with email data.'''

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    r = requests.post(url, json=value)
    print(r.rext)
