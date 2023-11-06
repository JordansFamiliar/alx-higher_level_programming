#!/usr/bin/python3
"""
This Python script accepts a URL as a command-line argument,
sends an HTTP GET request to the URL,
and then displays the response body. If the response status
code is less than 400, it prints the body;
otherwise, it prints an error message along with the status code.
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

        # Get the status code from the response
        status = response.status_code

        if status < 400:
            print(response.text)
        else:
            print("Error code: {}".format(status))
