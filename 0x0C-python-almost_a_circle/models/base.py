#!/usr/bin/python3
"""
This module contains the base class for all models.
"""


import csv
import json


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
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This method returns the JSON string
        representation of a list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to json file"""
        filename = cls.__name__ + ".json"
        text = "[]"
        if list_objs is None or len(list_objs) == 0:
            return text
        if list_objs is not None:
            for lst in list_objs:
                text.append(lst.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as f:
            return f.write(Base.to_json_string(text))

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
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """This method returns a list of instances of the class."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                text = f.read()
        except FileNotFoundError:
            return []
        return [cls.create(**d) for d in Base.from_json_string(text)]

    @classmethod
    def load_from_file_csv(cls):
        objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dic = {"id": int(row[0]),
                           "width": int(row[1]),
                           "height": int(row[2]),
                           "x": int(row[3]),
                           "y": int(row[4])}
                if cls.__name__ == "Square":
                    dic = {"id": int(row[0]),
                           "size": int(row[1]),
                           "x": int(row[2]),
                           "y": int(row[3])}
                o = cls.create(**dic)
                objs.append(o)
        return objs
