#!/usr/bin/python3
"""A script that takes a URL and sends a POST"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}

    data = urllib.parse.urlencode(data).encode()

    req = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
