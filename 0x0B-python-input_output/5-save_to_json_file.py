#!/usr/bin/python3

"""Defines an Object to text file (using JSON) function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using JSON representation"""
    with open(filename, "w") as f:
        obj = json.dumps(my_obj)
        write_data = f.write(obj)
    return write_data
