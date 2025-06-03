#!/usr/bin/python3
"""module that return the dict desciption with simple data struct
"""


def class_to_json(obj):
    """return the dictionnary of the obj
    """
    return obj.__dict__
