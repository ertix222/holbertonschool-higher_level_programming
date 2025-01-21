#!/usr/bin/python3
def no_c(my_string):
    nstr = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            nstr += char
    return nstr