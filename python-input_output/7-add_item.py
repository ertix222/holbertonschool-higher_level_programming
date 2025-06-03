#!/usr/bin/python3
"""module that adds items to a list and saves them in a JSON file
"""

import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""import json, sys and custom JSON save/load function
"""


filename = "add_item.json"

try:
    list = load_from_json_file(filename)
except FileNotFoundError:
    list = []

save_to_json_file(list, filename)
