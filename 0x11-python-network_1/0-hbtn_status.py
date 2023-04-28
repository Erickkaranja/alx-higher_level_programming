#!/usr/bin/python3
'''fetching internet resources using urllib package.'''

import urllib.request

if __name__ == '__main__':
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as out:
        content = out.read()
        print("Body response:")
        print("\t -type: {}".format(type(content)))
        print("\t -content: {}".format(content))
        print("\t -utf8content: {}".format(content.decode("utf-8")))
