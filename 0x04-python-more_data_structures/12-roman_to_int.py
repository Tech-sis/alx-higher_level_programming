#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = [data[x] for x in roman_string] + [0]
    rep = 0
    
    for i in range(len(num) - 1):
        if num[i] >= num[i+1]:
            rep += num[i]
        else:
            rep -= num[i]
            
    return rep
