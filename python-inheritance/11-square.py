#!/usr/bin/python3
"""
module 10-square
"""

Rectangle = __import__('9-rectangle').Rectangle
"""
here we import Rectangle from the file selected
"""


class Square(Rectangle):
    """
    create a square class
    """

    def __init__(self, size):

        self.integer_validator("size", size)
        self.__size = size

    def area(self):

        return (self.__size * self.__size)

    def __str__(self):

        return (f"[Square] {self.__size}/{self.__size}")
