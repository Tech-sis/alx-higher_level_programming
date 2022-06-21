#!/usr/bin/python3
"""
Define a class Square with private attribute
"""


class Square:
    """
    A square class with private attribute

    Parameters:
        size: the size of the square
    """

    def __init__(self, size):
        self.__size = size
