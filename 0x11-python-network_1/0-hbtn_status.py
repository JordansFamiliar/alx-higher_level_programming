#!/usr/bin/python3
"""A script that fetches the status of a url"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')
    as response:
        html = response.read()
        content_type = type(html)
        utf8_content = html.decode('utf-8')
        print("Body response:")
        print(f"    - type: {content_type}")
        print(f"    - content: {html}")
        print(f"    - utf8 content: {utf8_content}")
