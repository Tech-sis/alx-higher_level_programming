#!/usr/bin/python3
"""Defines aRectangle"""


class Rectangle:
    """
    A Rectangle class with private attribute and exceptions.
    Return the current area of rectangle

    Parameters:
        width: the width of the rectangle
        height: the height of the rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0:
            return 0
        if self.width == 0:
            return 0
        return 2 * (self.height + self.width)
