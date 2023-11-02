#!/usr/bin/env bash
#A script that takes a URL, sends a request to it, and
#displays the size of the body of the response.

url="$1"

size_download=$(curl -w "%{size_download}" -o /dev/null -s "$url")

echo "$size_download"
