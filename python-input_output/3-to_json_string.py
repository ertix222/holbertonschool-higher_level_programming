#!/usr/bin/python3
"""
defines a fonction that retuns
the JSON representation of an object
"""
import json
"""
import json to be use later
"""


def to_json_string(my_obj):
    """
    use of json.dumps() to convert obj to JSON chain
    """
    return json.dumps(my_obj)
