#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the body of the response.
"""
from sys import argv:
import requests


if __name__ == '__main__':
    url = argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
