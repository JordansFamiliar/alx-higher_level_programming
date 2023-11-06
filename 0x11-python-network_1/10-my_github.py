#!/usr/bin/python3
"""
Python script that accepts GitHub credentials (username and password)
and uses the GitHub API to fetch and display the user's ID.
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == '__main__':
    # Ensure the script is executed as the main program
    if len(argv) != 3:
        print("Usage: python script.py <GitHubUsername> <GitHubPassword>")
    else:
        # Construct the URL to access the GitHub user information
        username = argv[1]
        url = f'https://api.github.com/users/{username}'

        # Send a GET request to the GitHub API with authentication
        password = argv[2]
        auth = HTTPBasicAuth(username, password)
        response = requests.get(url, auth=auth)

        # Extract and display the user ID from the API response
        user_id = response.json().get('id')
        if user_id is not None:
            print(user_id)
