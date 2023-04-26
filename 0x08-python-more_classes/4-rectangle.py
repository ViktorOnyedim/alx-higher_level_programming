#!/usr/bin/python3

"""Defines a class Rectangle"""


class Rectangle:
    """Class rectangle is defined"""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieve the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
            return perimeter
        else:
            perimeter = 2 * (self.__width + self.__height)
            return perimeter

    def __str__(self):
        """Print the rectangle with the character '#'"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = ""
        for i in range(self.__height):
            rect += "#" * self.__width + '\n'
        return rect[:-1]

    def __repr__(self):
        """Return string representation of the rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect
