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

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[1] < 0 or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        else:
            for sym in range(0, self.position[1]):
                print("")
            for sym in range(0, self.__size):
                for char in range(0, self.position[0]):
                    print(" ", end="")
                for char in range(0, self.__size - 1):
                    print("#", end="")
                print("#")
