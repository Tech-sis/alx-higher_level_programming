#!/usr/bin/python3
"""This module implements the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class implements the Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter method"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter method"""
        self.width = value
        self.height = value

    def __str__(self):
        """custom __str__ method for Square"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__, self.id,
                                             self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args is not None and len(args) > 0:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        elif kwargs is not None:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns a dictionary representation of the Square"""
        return {'id': self.id, 'x': self.x, 'y': self.y, 'size': self.size}
