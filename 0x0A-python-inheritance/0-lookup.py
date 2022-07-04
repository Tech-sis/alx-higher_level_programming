#!/usr/bin/python3
"""A Function that returns the list of available attributes and methods"""


def lookup(obj):
    """Return the list of available attributes and methods"""
    return dir(obj)
