#!/usr/bin/python3
"""Defines an object to JSON function"""
import json


def to_json_string(my_obj):
    """
        Returns:
            JSON representation of an object (string)
    """
    json_obj = json.dumps(my_obj)
    return json_obj
