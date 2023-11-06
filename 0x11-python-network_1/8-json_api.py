#!/usr/bin/python3
"""
This Python script accepts a letter as a
command-line argument, sends a POST request
"""

import requests
from sys import argv

if __name__ == '__main__':
    letter = argv[1]

    # Define the URL for the POST request
    url = 'http://0.0.0.0:5000/search_user'

    # Send a POST request to the URL with the letter as a parameter
    response = requests.post(url, data={'q': letter})

    try:
        # Attempt to parse the response as JSON
        response_data = response.json()
        id, name = response_data.get('id'), response_data.get('name')
        if not response_data or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except Exception:
        print("Not a valid JSON")
