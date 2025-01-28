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

    def __init__(self, size=0, position=(0, 0)):

        """
        private instance attribute

        square with optional size
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """
        getter: property to retrieve
        the private attribute position
        """
        return self.__position

    @property
    def size(self):
        """
        getter: property to retrieve
        the private attribute size
        """
        return self.__size

    @position.setter
    def position(self, value):
        """
        property to set the position
        """
        pass
        if (not isinstance(value, tuple) or\
            len(value) != 2 or\
            not all(isinstance(num, int) and num >= 0 for num in value)):
            
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, value):

        """
        property to set the size
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

    def my_print(self):
        """
        public instance method
        print in stdout the square with '#'
        """
        if self.__size == 0:
            print()
            return
        
        for _ in range (self.__position[1]):
            print()
        
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
