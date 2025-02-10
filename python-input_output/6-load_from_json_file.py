#!/usr/bin/python3
"""
Module to load an object from a JSON file.
"""
import json
"""
Importing the json module for deserialization.
"""


def load_from_json_file(filename):
    """
    Read a JSON file
    and return the corresponding Python object.
    """
    with open(filename, "r", encoding="utf-8")as f:
        return json.load(f)
