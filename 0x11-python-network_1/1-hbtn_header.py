#!/usr/bin/python3
"""A script that takes in a URL and sends a request"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.info().get('X-Request-Id')
        print(x_request_id)
