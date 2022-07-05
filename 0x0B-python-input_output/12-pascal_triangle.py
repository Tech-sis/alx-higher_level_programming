#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """Prints pascal triangle"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    pascal = [[1]]
    for rows in range(n-1):
        pascal.append([a+b for a, b
                       in zip([0] + pascal[-1], pascal[-1] + [0])])

    return pascal
