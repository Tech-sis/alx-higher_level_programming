#!/usr/bin/python3
def uppercase(str):
    for i in ord(str):
        if (i >= 65) and (i <= 90):
            print("{}".format(chr(str)))
        if (i >= 97) and (i <= 122):
            print("{}".format(chr(str)), end='')
