#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)

    j = 0
    new = my_string[:]

    for i in range(length):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            new = new[:(i - j)] + my_string[(i + 1):]
            j += 1

    return (new)
