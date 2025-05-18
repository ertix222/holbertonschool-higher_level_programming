#!/usr/bin/python3

"""
Module 0-add_integer
This module provides a function `add_integer` that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers a and b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a+b
