#!/usr/bin/python3

"""Base geometry module
"""


class BaseGeometry():
    """class basegeometry
    """
    def area(self):
        """Raise an exception (not implemented)
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value: must be int > 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
