#!/bin/bash
# Sends a GET request to a URL, and displays the body of the response
curl -s -w '%{http_code}' -o /dev/null "$1"
