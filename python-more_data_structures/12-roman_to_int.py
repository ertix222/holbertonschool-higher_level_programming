#!/usr/bin/python3
def roman_to_int(roman_string):
    rNum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    total, prev_value = 0, 0
    for c in roman_string[::-1]:
        value = rNum[c]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total
