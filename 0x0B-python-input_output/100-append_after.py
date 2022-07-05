#!/usr/bin/python3
"""
This module creates an Object from a “JSON file”:
"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r', encoding="utf-8") as f:
        content = f.readlines()
        for (i, line) in enumerate(content):
            if line.find(search_string) != -1:
                content.insert(i+1, new_string)
        new_content = "".join(content)
    f = open(filename, 'w')
    f.write(new_content)
    f.close()
