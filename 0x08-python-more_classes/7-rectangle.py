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

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.height == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """
        String representation of rectangle so call to print works
        Example: print(my_rectangle)
        """

        text = ''
        if self.height == 0 or self.width == 0:
            return text
        text += '\n'.join([str(self.print_symbol)
                          * self.width for rows in range(self.height)])
        return text

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def my_print(self):
        """
        Prints the rectangle
        """
        if self.width == 0 or self.height == 0:
            print()
        else:
            for i in range(self.height):
                print("#" * self.width)
        return None
