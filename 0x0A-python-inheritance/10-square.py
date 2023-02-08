#!/usr/bin/python3

"""Defines a Square class"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size):
        """Instantiates a square object"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Computes the area of the square"""
        try:
            return self.__size ** 2
        except Exception:
            raise Exception("area() is not implemented")
