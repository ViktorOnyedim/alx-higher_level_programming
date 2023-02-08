#!/usr/bin/python3

"""Defines a class and inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class
    Args:
        obj (any): Object to checked
        a_class (class): The class to match the type of obj to.
    Returns:
        True - if the object is an instance of or inherited instance of class
        False - Otherwise
    """
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
