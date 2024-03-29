#!/usr/bin/python3
"""Convert from JSON to Python Object"""

import json


def from_json_string(my_str):
    """
    Parses a JSON object and returns the corresponding python object
    """
    return json.loads(my_str)
