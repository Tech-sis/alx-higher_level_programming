#!/usr/bin/python3
"""
Define a class Square
"""


class Square:
    """
    A square class with private attribute and exceptions.
    Return the current square area

    Parameters:
        size: the size of the square
    """

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def __eq__(self, other):
        """
        Compares and returns if equal
        """
        return self.size == other.size

    def __ne__(self, other):
        """
        Compares and returns if not equal
        """
        return self.size != other.size

    def __gt__(self, other):
        """
        Compares and returns if greater than
        """
        return self.size > other.size

    def __ge__(self, other):
        """
        Compares and returns if greater than or equal
        """
        return self.size >= other.size

    def __lt__(self, other):
        """
        Compares and returns if less than
        """
        return self.size < other.size

    def __le__(self, other):
        """
        Compares and returns if less than or equal
        """
        return self.size <= other.size
