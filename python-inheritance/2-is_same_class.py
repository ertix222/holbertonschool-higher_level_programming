#!/usr/bin/python3

"""
return if the object is exactly
an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Use 'type() is' to check if obj is exactly
    an instance of a_class
    """
    return type(obj) is a_class
