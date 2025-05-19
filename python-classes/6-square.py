#!/usr/bin/python3

"""
create a class Square
"""


class Square:
    """
    defines a square
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        size = self.size
        position = self.position
        if size == 0:
            print("")
        if position[1] > 0:
            for _ in range(position[1]):
                print("")
        if position[0] >= 0:
            for _ in range(self.__size):
                print(" " * position[0] + "#" * self.__size)
