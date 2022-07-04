#!/usr/bin/python3
"""
This module returns True if it is the exact instance of the class
"""


def is_same_class(obj, a_class):
    """implementation
    Args:
        obj (Any): object to check
        a_class (type): type to check against
    Returns:
        [boolean]: response
    """
    return type(obj) == a_class
