#!/usr/bin/python3
"""
This Python script accepts a URL as a command-line argument,
sends an HTTP request to the URL,
and then extracts and displays the value of the 'X-Request-Id'
field from the response headers.
"""

import requests
from sys import argv

if __name__ == '__main__':
    # Ensure the script is executed as the main program
    if len(argv) != 2:
        print("Usage: python script.py <URL>")
    else:
        # Retrieve the URL from the command-line argument
        url = argv[1]

        # Send an HTTP GET request to the specified URL
        response = requests.get(url)

        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(f"X-Request-Id: {x_request_id}")
