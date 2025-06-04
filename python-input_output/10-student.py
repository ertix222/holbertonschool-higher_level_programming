#!/usr/bin/python3
"""module that instance age and name
and retrieves a dictionary representation
"""


class Student:
    """class that defines a student
    """
    def __init__(self, first_name, last_name, age):
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(
            isinstance(item, str) for item in attrs
        ):
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__
