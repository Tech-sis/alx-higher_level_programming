#!/usr/bin/python3
"""
This module opens a file and print it to stdout
"""


def write_file(filename="", text=""):
    """
    This function opens a file and print its content
            Parameters:
                filename (string): A string that holds a filename
                value (string): prints content to stdout
    """
    with open(filename, encoding="utf-8") as f:
        print(f.write(text), end='')
