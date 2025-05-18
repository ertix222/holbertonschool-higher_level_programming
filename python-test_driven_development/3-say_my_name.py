#!/usr/bin/python3


"""
this module print both first and last name
passed as arguments
"""


def say_my_name(first_name, last_name=""):

    """
    checks for string only as arguments
    if not, raise error
    then  performs the print
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
