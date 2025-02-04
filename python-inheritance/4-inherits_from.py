#!/usr/bin/python3
"""
module 4-inherits_from

return true if obj is an instance
otherwise False
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherits
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
