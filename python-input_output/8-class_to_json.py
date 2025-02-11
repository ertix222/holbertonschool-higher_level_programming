#!/usr/bin/python3
"""
Module that provides a function to convert an object
into a dictionary representation for JSON serialization
"""


def class_to_json(obj):
    """
    returns the dictionary description
    of an object for JSON serialization 
    """
    return obj.__dict__
