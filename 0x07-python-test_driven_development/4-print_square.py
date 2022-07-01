#!/usr/bin/python3
"""
This modules prints a square with #
The function prints a squre
"""


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

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
