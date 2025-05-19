#!/usr/bin/python3

"""
create a class Square
"""


class Square():
    """
    defines a square
    """

    def __init__(self, size=0):

        """
        define the size of the square
        in a privates instance
        """

        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size musts be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):

        """
        return the area of the square
        """

        return (self.__size ** self.__size)
