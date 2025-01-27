#!/usr/bin/python3

"""
module 0-square

Function:
create a square class
"""


class Square:

    """
    This is my classe
    for a square
    """

    def __init__(self, size=0):

        """
        methods for the square
        with his size
        """
        self.__size = size
        pass
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
