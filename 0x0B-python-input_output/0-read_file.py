#!/usr/bin/python3
"""This module reads a text file (UTF8)"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout
    Args:
        filename: Name of the file to read from
    """
    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
    print(read_data, end="")
