#!/usr/bin/python3
"""Defines a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)
    Args:
        filename: Name of the file to write to
    Return:
        Number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        write_data = f.write(text)
    return write_data
