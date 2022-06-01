#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100):
        if (i % 3 == 0):
            print("Fizz", end='')
            continue
        if (i % 5 == 0):
            print("Buzz", end='')
            continue
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz", end='')
            continue
        else:
            print("{} ".format(i), end='')
    # print("{} ".format(i), end='')
    return i
            