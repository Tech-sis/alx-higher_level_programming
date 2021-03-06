#!/usr/bin/python3
"""
Module 9-rectangle
Contains parent class BaseGeometry
with public instance method area and integer_validator
Contains subclass Rectangle
with instantiation of private attributes width and height, validated by parent
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry
    Methods:
        __init__(self, width, height)
    """

    def __init__(self, width, height):
        """validate and initialize width and height
        Args:
            width (int): private
            height (int): private
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
