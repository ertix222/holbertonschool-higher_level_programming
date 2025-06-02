#!/usr/bin/python3
"""module that saves an object to a file using JSON format
"""

import json
"""importation of json module
"""


def save_to_json_file(my_obj, filename):
    """write an object to a text file using JSON representation.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
