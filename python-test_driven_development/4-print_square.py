#!/usr/bin/python3
"""
module that print_square
"""


def print_square(size):
    """
    checking if it's an integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for a in range(size):
        for b in range(size):
            print("#", end="")
        print()