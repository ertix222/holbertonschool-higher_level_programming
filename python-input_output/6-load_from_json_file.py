#!/usr/bin/python3
"""module for loading an object from a JSON file
"""

import json
"""importation of json module
"""


def load_from_json_file(filename):
    """load and return an object from a JSON file
    """
    with open(filename, 'r', encoding="UTF-8") as file:
        return json.load(file)
