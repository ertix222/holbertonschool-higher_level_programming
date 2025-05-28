#!/usr/bin/python3

"""Rectangle module
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""import BaseGeometry
"""


class Rectangle(BaseGeometry):
    """class Rectangle
    """
    def __init__(self, width, height):
        """initialize a rectanlge with width and height
        """
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height
