#!/usr/bin/python3

"""
module 1-Rectangle

Function:
create a Rectangle class
"""


class Rectangle:

    """
    This is a class for a Rectangle
    """

    def __init__(self, width=0, height=0):

        """
        private instance attribute
        with optional width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        getter: property to retrieve
        the private attribute width
        """
        return self.__width

    @property
    def height(self):
        """
        getter: property to retrieve
        the private attribute height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        setter: property to set it
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        setter: property to set it
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
