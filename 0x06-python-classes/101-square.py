#!/usr/bin/python3
"""
This module defines a Square class
Its implements value and type checks for its attributes
Attributes:
    area
    my_print
"""


class Square:
    """Square implementation
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if type(position) != tuple or \
            len(position) != 2 or \
            not all(isinstance(el, int) for el in position) or \
                not all(el >= 0 for el in position):

            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position

    def area(self):
        """calculates the square area
        """
        return (self.size ** 2)

    def __str__(self):
        """
        String representation of square so call to print works
        Example: print(my_square)
        """
        txt = ''
        if (self.__size == 0):
            return txt

        txt += '\n' * self.position[1]
        txt += '\n'.join([" " * self.__position[0] + "#" *
                         self.__size for rows in range(self.__size)])
        return txt

    def my_print(self):
        """prints a square  with the corresponding size
        """
        if (self.__size == 0):
            return txt

        print('\n' * self.position[1], end="")
        print('\n'.join([" " * self.__position[0] + "#" *
                         self.__size for rows in range(self.__size)]))
