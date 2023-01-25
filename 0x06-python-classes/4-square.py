#!/usr/bin/python3

"""Define a class Square"""

class Square:
    """Class square is defined
    Args:
        size (int): size of the square
    """
    def __init(self, size=0):
        self.__size = size

    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    def size(self, value=0):
        """Set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2
