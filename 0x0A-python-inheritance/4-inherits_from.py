#!/usr/bin/python3
"""
This module implements  a function that returns True if the object
is an instance of a class that inherited (directly or indirectly)
- the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """implementation
    Args:
        obj (Any): object to check
        a_class (type): type to check against
    Returns:
        boolean: response
    """
    return type(obj) != a_class and issubclass(type(obj), a_class)
