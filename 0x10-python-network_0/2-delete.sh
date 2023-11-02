#!/usr/bin/env bash
#A script that sends a DELETE request to the URL
#passed as the first argument and displays the body
#of the response.

url="$1"

curl -X DELETE -s "$url"
