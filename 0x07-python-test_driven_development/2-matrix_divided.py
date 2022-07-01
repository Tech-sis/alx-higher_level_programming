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

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
