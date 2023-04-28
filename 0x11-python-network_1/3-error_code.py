#!/usr/bin/python3
'''script that send a request to a url and the body of the response.'''

import sys
import urllib.request
import urllib.error.HTTPError

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("ascii"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
