#!/bin/bash
#A script that takes in a URL and displays all HTTP methods
curl -Is "$1" | grep -i '^Allow:' | tr -d '\r' | cut -d' ' -f2-
