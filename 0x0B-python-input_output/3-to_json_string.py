#!/usr/bin/python3
"""
This module returns the JSON representation of an object(string)
"""


import json


def to_json_string(my_obj):
    """
    This function returns the JSON representation of an object(string)
            Parameters:
                my_obj (string): A string 
                value (string): returns json
    """
    return json.dumps(my_obj)
