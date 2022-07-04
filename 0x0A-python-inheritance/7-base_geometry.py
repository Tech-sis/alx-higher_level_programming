#!/usr/bin/python3
"""
This module is a class with a public instance
"""


class BaseGeometry:
    """This class has a public instance area that raises an exception"""

    def area(self):
        """This function raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This function validates value
            Parameters:
                name (string): A string
                value (int): A decimal integer
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
