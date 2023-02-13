#!/usr/bin/python3
"""Defines an append-string function"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    Args:
        filename: The name of the file to append to
        text: Text to be appended
    Returns:
        The number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        chars_added = f.write(text)
    return chars_added
