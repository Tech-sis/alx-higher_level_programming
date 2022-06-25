#!/usr/bin/python3
"""
This modules prints a square with #
The function prints a squre
"""


from math import floor


def print_square(size):
    """prints a square
        Args:
        size int: term 1
    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    Returns:
        str: prints a square with character #
    """
    if type(size) != int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif type(size) == float and size < 0:
        raise TypeError('size must be an integer')

    if (size == 0):
        print('')
    if (type(size) == float):
        floor(size)

    for i in range(size):
        print('#' * size)
