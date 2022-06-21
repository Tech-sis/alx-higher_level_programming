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
        """
        calculates the square area
        """
        return self.__size * self.__size

    def my_print(self):
        """
        prints the square using #
        """
        if (self.__size == 0):
            print('')

        for i in range(self.__size):
            print('#' * self.__size)
