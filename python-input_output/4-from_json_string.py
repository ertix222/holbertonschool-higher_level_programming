#!/usr/bin/python3
"""
defines a fonction that return
an object represented by a JSON string
"""
import json
"""
import json to be use later
"""


def from_json_string(my_str):
    """
    use of json.loads() to convert obj to JSON string
    """
    return json.loads(my_str)
