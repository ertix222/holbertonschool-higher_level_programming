#!/usr/bin/python3
"""return a python data structure represented by a JSON string
"""

import json
"""importation of json
"""


def from_json_string(my_str):
    """function that return my_str represented by a JSON string
    """
    return json.loads(my_str)
