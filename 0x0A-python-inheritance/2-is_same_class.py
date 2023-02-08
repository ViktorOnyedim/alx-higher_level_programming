#!/usr/bin/python3

"""
    This module defines a function that checks if the object is exactly and instance of the specified class
"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check
    Returns:
        True if the object is exactly instance of specified class
        Otherwise False
    """
    return (type(obj) is a_class)
