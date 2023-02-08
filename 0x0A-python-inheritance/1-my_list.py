#!/usr/bin/python3

"""This module inherits from the list class"""


class MyList(list):
    """Defines MyList class that inherits from list class"""
    def print_sorted(self):
        """print the list, but sorted (ascending sort)"""
        sorted_list = sorted(self)
        print(sorted_list)
