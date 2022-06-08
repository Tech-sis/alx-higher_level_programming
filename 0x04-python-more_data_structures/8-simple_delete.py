#!/usr/bin/python3
from re import A


def simple_delete(a_dictionary, key=""):
    a_dictionary.pop(key, None)
    return a_dictionary
