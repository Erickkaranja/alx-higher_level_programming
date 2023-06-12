#!/usr/bin/python3
'''takes url as argv and returns header content.'''

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as out:
        print(out.headers)
