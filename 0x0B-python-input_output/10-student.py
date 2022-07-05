#!/usr/bin/python3
"""This module defines a class student"""


class Student:
    """
        Instantiating the instance methods of the class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        if not isinstance(attrs, list):
            return self.__dict__
        for index in attrs:
            if not isinstance(index, str):
                return self.__dict__
        dictionary = {}
        for index in attrs:
            try:
                dictionary[index] = self.__dict__[index]
            except:
                pass
        return dictionary
