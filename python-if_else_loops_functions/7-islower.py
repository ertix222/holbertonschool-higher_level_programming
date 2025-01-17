#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:  # Minuscule
        return "{c} is lower"
    elif ord(c) >= 65 and ord(c) <= 90:  # Majuscule
        return "{c} is upper"
    else:
        return False
    