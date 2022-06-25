#!/usr/bin/python3
"""
This module defines `say_my_name`
A function prints first and last name
"""


def say_my_name(first_name, last_name=""):
    """prints a name
    Args:
        first_name str: term 1
        last_name str: term 2.
    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    Returns:
        str: My name is <first_name> <last_name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
