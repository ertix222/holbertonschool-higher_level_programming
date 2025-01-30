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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        """
        private instance attribute
        with optional width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Public instance method
        that returns the rectangle area
        """
        area = self.height * self.width
        return area

    def perimeter(self):
        """
        Public instance method
        that returns the rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            perimeter = 0
            return perimeter
        else:
            perimeter = (self.height + self.width) * 2
            return perimeter

    def __str__(self):
        """
        Returns a string representation of the rectangle using #
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return "\n".join(
                str(self.print_symbol) * self.width
                for _ in range(self.height)
                )

    def __repr__(self):
        """
        Returns a string representation that allows instance recreation
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        print a message when an instance is delete
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method that returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1
