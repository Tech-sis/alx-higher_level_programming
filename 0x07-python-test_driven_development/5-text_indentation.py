#!/usr/bin/python3
"""
This module defines `text_indentation`
The function prints a text with 2 new lines after each of
these characters: ., ? and :
"""


def text_indentation(text):
    """adds paragraph after `.`, `:` and `?`
    Args:
        text (str)
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
