#!/usr/bin/python3
'''Python script that takes in a URL and an email,
   sends a POST request to the passed URL with the email as a parameter.'''

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    params = urllib.parse.urlencode(value)
    params = params.encode("ascii")
    req = urllib.request.Request(url, params)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
