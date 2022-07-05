#!/usr/bin/python3
"""
This module appends to a file and return the number of character
"""


def append_write(filename="", text=""):
    """
    This function appends to a file and return the number of character
            Parameters:
                filename (string): A string that holds a filename
                value (string): prints content to stdout
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
