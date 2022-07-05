#!/usr/bin/python3
"""
This module writes an Object to a text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an Object to a text file, using a JSON representation
            Parameters:
                my_obj (string): A string
                filename: points to a file
                value (string): returns python data structure
    """
    with open(filename, encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
