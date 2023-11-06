#!/usr/bin/python3
"""
This script takes a URL and an email address as arguments,
sends a POST request to the specified URL with the email as a parameter,
and then displays the content of the response body.
"""

import requests
from sys import argv

if __name__ == '__main__':
    # Ensure the script is executed as the main program
    if len(argv) != 3:
        print("Usage: python script.py <URL> <email>")
    else:
        # Extract the URL and email from command-line arguments
        url = argv[1]
        email = argv[2]

        # Create a dictionary payload with the email parameter
        payload = {'email': email}

        # Send a POST request to the URL with the payload
        response = requests.post(url, data=payload)

        # Display the content of the response body
        print(response.text)
