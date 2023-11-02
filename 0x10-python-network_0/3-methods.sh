#!/usr/bin/env bash
#A script that takes in a URL and displays all HTTP methods
#the server will accept.

url="$1"

curl -Is "$url" | grep -i '^Allow:' | tr -d '\r' | cut -d' ' -f2-
