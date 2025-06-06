#!/usr/bin/python3
import json
"""import json module
"""

def serialize_and_save_to_file(data, filename):
    """save data to a JSON file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_and_deserialize(filename):
    """load data from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)