#!/usr/bin/python3

"""
module 0-square

Function:
create a square class
"""


class Square:

    """
    This is my classe for a square
    """

    def __init__(self, size=0):

        """
        private instance attribute

        square with optional size
        """
        self.size = size

    @property
    def size(self):
        """
        getter: property to retrieve the private size
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        property to set it
        """
        pass
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """
        public instance method

        that returns the square area
        """
        return self.__size ** 2