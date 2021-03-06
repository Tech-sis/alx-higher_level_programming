#!/usr/bin/python3
"""
This module opens a file and print it to stdout
"""


def read_file(filename=""):
    """
    This function opens a file and print its content
            Parameters:
                filename (string): A string that holds a filename
                value (string): prints content to stdout
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
