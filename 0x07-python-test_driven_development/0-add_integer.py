#!/usr/bin/python3
"""
This module defines `add_integer`
The function returns the sum of a and b
"""


def add_integer(a, b=98):
    """adds a and b
    Args:
        a (int): term 1
        b (int, optional): term 2. Defaults to 98.
    Raises:
        TypeError: a and b must be integer
    Returns:
        int: sum of a and b
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
