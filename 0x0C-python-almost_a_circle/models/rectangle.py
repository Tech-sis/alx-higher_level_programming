#!/usr/bin/python3
"""
This module implements the Rectangle class.
"""


from models.base import Base


class Rectangle(Base):
    """
    The following are getters and setters for the Rectangle class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        ''''Initializes the class Rectangle'''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    # @property
    # def id(self):
    #     return super().__init__(id)

    # @id.setter
    # def id(self, value):
    #     if type(value) != int:
    #         raise TypeError("id must be an integer")
    #     # super().__init__(id)  # call the parent class' __init__ method

    def area(self):
        """returns the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """prints in stdout the Rectangle instance with the character '#' """
        for jump in range(self.y):
            print()
        for row in range(self.height):
            for space in range(self.x):
                print(" ", end="")
            for column in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """returns a string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args is not None and len(args) > 0:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        elif kwargs is not None:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns dictionary representation of the rectangle"""
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
