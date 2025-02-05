#!/usr/bin/python3
"""
module 8-rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
here we import Base Geometry from the file 7-base_Geometry
"""


class Rectangle(BaseGeometry):
    """
    class of a Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle with width and height.
        """
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height
