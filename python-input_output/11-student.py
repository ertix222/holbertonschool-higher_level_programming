#!/usr/bin/python3
"""
Module to defining the Student class
"""


class Student:
    """
    represents a student with a first name
    last name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        initialize Student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        return the dictionary representation of the student instance
        """
        if isinstance(attrs, list) and all(
            isinstance(item, str) for item in attrs
        ):
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__

    def reload_from_json(self, json):
        """
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
