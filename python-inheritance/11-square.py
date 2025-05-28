#!/usr/bin/python3

"""Square module
"""

Rectangle = __import__("9-rectangle").Rectangle
"""import Rectangle
"""


class Square(Rectangle):
    """class Square that inherite from Rectangle
    """
    def __init__(self, size):
        """initialize a Square with is size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """get hte area of the square
        """
        return (self.__size * self.__size)

