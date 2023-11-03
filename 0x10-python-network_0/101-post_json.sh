#!/bin/bash
#Sends a JSON POST request to a URL
curl -X POST -d "@$2" -H "Content-Type: application/json" -s "$1"
