#!/usr/bin/python3
"""
Module to save an object to a JSON file
"""
import json
"""
import json module for serialization
"""


def save_to_json_file(my_obj, filename):
    """
    write an object to a text file
    using JSON representation
    """
    with open(filename, "w", encoding="utf-8")as f:
        f.write(json.dumps(my_obj))
