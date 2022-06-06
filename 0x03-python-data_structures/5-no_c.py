#!/usr/bin/env python3
def no_c(my_string):
    for char in my_string:
        if char == 'c' or char == 'C':
            new = char.pop()
    return (new)
