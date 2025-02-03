#!/usr/bin/python3
"""
module 2-is_same_class

Fonction:
return True if the object
is the specified class
otherwise return False
"""


def is_same_class(obj, a_class):
    """
    module for compare class
    """
    return type(obj) is a_class
