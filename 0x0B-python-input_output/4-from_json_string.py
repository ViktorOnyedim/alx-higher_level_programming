#!/usr/bin/python3
"""Convert from JSON to Python Object"""

import json


def from_json_string(my_str):
    py_obj = json.loads(my_str)
    return py_obj
