#!/usr/bin/python3
"""
Takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
import requests

if __name__ == '__main__':
    letter = "" if len(argv) == 1 else argv[1]
    url = "http://0.0.0.0:5000/search_user"

    r = request.post(url, data={'q': letter})
    try:
        response = r.json()
        if response:
            print(f"[{response['id']}] {response['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
