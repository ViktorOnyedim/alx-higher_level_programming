#!/usr/bin/python3
"""
Takes a URL, sends a request to a URL and displays the value of
the 'X-Request-Id' variable found in the header of the response
"""

from sys import argv
import urllib.request

url = argv[1]
with urllib.request.urlopen(url) as response:
    headers = response.info()
    x_request_id = headers.get('X-Request-Id')
    print(x_request_id)
