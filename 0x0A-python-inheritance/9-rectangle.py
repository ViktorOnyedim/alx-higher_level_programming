#!/usr/bin/python3

"""Defines a class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle"""
    def __init__(self, width, height):
        """Instantiates an object"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Find area of base geometry

        Raises:
            Exception: "area() is not implemented"
        """
        try:
            return (self.__width * self.__height)
        except Exception:
            raise Exception("area() is not implemented")

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
