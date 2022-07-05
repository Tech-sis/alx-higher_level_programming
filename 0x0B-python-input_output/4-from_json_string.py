#!/usr/bin/python3
"""
This module returns an object (Python data structure)
represented by a JSON string
"""


import json


def from_json_string(my_str):
    """
    This function returns an object (Python data structure)
    represented by a JSON string
            Parameters:
                my_str (string): A string
                value (string): returns python data structure
    """
    return json.loads(my_str)
