#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100):
        if (i % 3 == 0):
            print("Fizz")
        if (i % 5 == 0):
            print("Buzz")
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
    print("{} ".format(i), end='')
    return i
            