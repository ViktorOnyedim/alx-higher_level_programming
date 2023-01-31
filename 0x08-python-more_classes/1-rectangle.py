#!/usr/bin/python3

"""Defines a rectangle"""


class Rectangle:
    """Class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the rectangle"""
        self.__height = height
        self.__width = width

    def width(self):
        """retrieve the width of the rectangle"""
        return self.__width

    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")       
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        
    def height(self):
        """Retrieve the height of the rectangle"""
        pass
    
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
