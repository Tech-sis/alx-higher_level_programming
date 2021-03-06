#!/usr/bin/python3
"""
This module contains the base class for all models.
"""


import csv
import json
import turtle


class Base:
    """
    This method returns the number of instances of the class.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """This method initializes the class."""

        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This method returns the JSON string
        representation of a list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to json file"""
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        This method returns the JSON string
        representation of a list of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """This method returns an instance of the class."""
        # if cls.__name__ == "Rectangle":
        #     dummy = cls(1, 1)
        # elif cls.__name__ == "Square":
        #     dummy = cls(1)
        # dummy.update(**dictionary)
        # return dummy
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                instance = cls(10, 5)
            else:
                instance = cls(10)
            instance.update(**dictionary)
            return instance

    @classmethod
    def load_from_file(cls):
        """This method returns a list of instances of the class."""
        filename = cls.__name__ + ".json"
        # try:
        #     with open(filename, mode="r", encoding="utf-8") as f:
        #         text = f.read()
        # except FileNotFoundError:
        #     return []
        # return [cls.create(**d) for d in Base.from_json_string(text)]
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                list_dict = Base.from_json_string(f.read())
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        :param list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        if filename == "Rectangle.csv":
            header = ["id", "width", "height", "x", "y"]
        else:
            header = ["id", "size", "x", "y"]

        with open(filename, "w", newline="") as csv_file:
            if list_objs == [] or list_objs is None:
                csv_file.write("[]")
            else:
                writer = csv.DictWriter(csv_file, fieldnames=header)
                for objs in list_objs:
                    writer.writerow(objs.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        return:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as csv_file:
                if cls.__name__ == "Rectangle":
                    header = ["id", "width", "height", "x", "y"]
                else:
                    header = ["id", "size", "x", "y"]
                list_objs = csv.DictReader(csv_file, fieldnames=header)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_objs]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
