#!/usr/bin/python3
"""
Module 10-square
Contains parent class BaseGeometry
with public instance method area and integer_validator
Contains subclass Rectangle
with instantiation of private attributes width and height, validated by parent
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from BaseGeometry
    Methods:
        __init__(self, size)
    """

    def __init__(self, size):
        """validate and initialize width and height
        Args:
            size (int): private
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
