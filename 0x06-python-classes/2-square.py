#!/usr/bin/python3
"""
Define a class Square with private attribute and raise exceptions
"""


class Square:
    """
    A square class with private attribute and exceptions

    Parameters:
        size: the size of the square
    """

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
