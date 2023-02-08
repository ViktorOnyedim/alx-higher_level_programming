#!usr/bin/python3

"""Defines a BaseGeometry class"""


class BaseGeometry:
    """Represents BaseGeometry"""
    def area(self):
        """
        This function finds area of base geometry

        Raises:
            Exception -> "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This function Validates an integer

        Args:
            name (string): name
            value (int): Integer value to be validated

        Returns:

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if (not isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
