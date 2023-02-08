#!/usr/bin/python3

"""Defines function that checks if object is inherited from specified class"""


def inherits_from(obj, a_class):
    """Checks if object is instance of a class inherited from specified class
    Args:
        obj (any): Object to check
        a_class (class): class to be checked
    Returns:
        True - if object is an instance of class that inherits from specified
        False - Otherwise
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
