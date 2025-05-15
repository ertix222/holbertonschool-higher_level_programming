#!/usr/bin/python3
def roman_to_int(roman_string):
    rNum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None or roman_string is not str:
        return 0
    if roman_string:
        print(f"{roman_string}, ")
