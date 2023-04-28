#!/usr/bin/python3
"""Fetches 'https://alx-intranet.hbtn.io/status'"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    data = response.read()
    decoded_data = data.decode("utf-8")
print("Body response:")
print(f"\t- type: {type(data)}")
print(f"\t- content: b'{decoded_data}'")
print(f"\t- utf8 content: {decoded_data}")
