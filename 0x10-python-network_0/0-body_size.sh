#!/bin/bash
#A script that takes a URL, sends a request to it
echo "$(curl -w "%{size_download}" -o /dev/null -s "$1")"
