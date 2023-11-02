#!/usr/bin/env bash
#A script that takes in a URL as an argument,
#sends a GET request to the URL AND
#displays the body of the response.

url="$1"

curl -H "X-School-User-Id: 98" -s "$url"
