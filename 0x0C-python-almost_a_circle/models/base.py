#!/usr/bin/python3
"""Defines a base class"""

import json


class Base:
    """Represents a base"""
    __nb_objects = 0

    def __init__(self, id=None):
        "Instantiates a base object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
            Parses a python list object and returns corresponding JSON object
        """
        if list_dictionaries == None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
