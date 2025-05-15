#!/usr/bin/python3
def roman_to_int(roman_string):
    rNum = {'i':1, 'v':5, 'x':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    if roman_string is None or roman_string is not str:
        return 0