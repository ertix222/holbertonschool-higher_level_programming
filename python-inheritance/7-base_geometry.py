#!/usr/bin/python3
"""
Module 7-base_geometry

containing the Basegeometry class.
"""


class BaseGeometry:
    """
    class for BaseGeometry
    """
    pass

    def area(self):
        """
        always lifted for every exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        methode to validate the integer
        """
        if not type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
