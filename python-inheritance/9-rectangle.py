#!/usr/bin/python3
"""
module 9-rectangle
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

    def area(self):
        """
        module for the area of the rectangle.
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        module for str to return the description
        """
        return (f"[Rectangle] {self.__width}/{self.__height}")
