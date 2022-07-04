#!/usr/bin/python3
"""
This function returns true if the object is an instance of the specified class
"""


def is_kind_of_class(obj, a_class):
    """implementation
    Args:
        obj (Any): object to check
        a_class (type): type to check against
    Returns:
        boolean: response
    """
    return isinstance(obj, a_class)
