#!/usr/bin/python3
"""
This module defines `add_integer`
The function returns the sum of a and b
"""


def matrix_divided(matrix, div):
    """divides elements in a matrix
    Args:
        matrix [(int) or (float)]: term 1
        div (int or float): term 2.
    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: division by zero
        TypeError: div must be a number
        ZeroDivisionError: division by zero
    Returns:
        list: division of matrix
    """
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    divided_matrix = [x[:] for x in matrix]
    for line in divided_matrix:
        if len(line) != len(divided_matrix[0]):
            raise TypeError("division by zero")

        for i, element in enumerate(line):
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

            line[i] = round(element/div, 2)
    return divided_matrix
