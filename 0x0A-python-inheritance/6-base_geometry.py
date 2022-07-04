#!/usr/bin/python3
"""
This module is a class with a public instance
"""


class BaseGeometry:
    """This class has a public instance area that raises an exception"""

    def area(self):
        """This function raises an exception"""
        raise Exception("area() is not implemented")
