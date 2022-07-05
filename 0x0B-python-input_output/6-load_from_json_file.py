#!/usr/bin/python3
"""
This module creates an Object from a “JSON file”:
"""


import json


def load_from_json_file(filename):
    """
    This function creates an Object from a “JSON file”:
            Parameters:
                filename: points to a file
                value (string): returns python data structure
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.loads())
