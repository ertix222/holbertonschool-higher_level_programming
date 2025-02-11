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

    def to_json(self):
        """
        return the dictionary representation of the student instance
        """
        return self.__dict__
