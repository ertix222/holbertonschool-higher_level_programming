#!/usr/bin/python3
"""return a json representation of an object
"""

import json
"""importation of json
"""


def to_json_string(my_obj):
    """function that return my_obj an a json representation
    """
    return json.dumps(my_obj)
