#!/usr/bin/python3
"""
This Python script is designed to solve a specific
challenge by making a request to the GitHub API.
"""

import requests
from sys import argv

if __name__ == '__main__':
    # Ensure the script is executed as the main program
    if len(argv) != 3:
        return
    else:
        # Construct the URL to access the latest commits
        owner = argv[2]
        repository_name = argv[1]
        url = f"https://api.github.com/repos/{owner}/{repository_name}/commits"

        # Send a GET request to the GitHub API
        response = requests.get(url)

        # Extract and display information about the latest 10 commits
        commits = response.json()
        for commit in commits[:10]:
            print(commit.get('sha'), end=': ')
            print(commit.get('commit').get('author').get('name'))
