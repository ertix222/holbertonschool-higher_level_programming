#!/usr/bin/python3
"""
module 3-is_kind_of_class

Fonction:
return True if the object is an instance
or if the object is an instance of a class that inherited from
otherwise return False
"""


def is_kind_of_class(obj, a_class):
    """
    module to Check if an object is a direct body
    or an instance of a subclass of a given class.
    """
    return isinstance(obj, a_class)
