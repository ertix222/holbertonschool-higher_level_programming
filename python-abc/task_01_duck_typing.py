#!/usr/bin/python3
"""
module task__01_duck_typing
"""
from math import pi
from abc import ABC, abstractmethod
"""
import ABC and abstracmethod from the abc module
and import pi from math
"""


class Shape(ABC):
    """
    Abstract base class for shapes
    """
    @abstractmethod
    def area(self):
        """
        Abstract method that must be implemented by subclasses
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape
        """
        pass


class Circle(Shape):
    """
    Circle class inheriting from Shape
    """
    def __init__(self, radius):
        """
        Initialize a Circle with a given radius
        """
        self.radius = radius

    def area(self):
        """
        Compute the area of the circle
        """
        return (pi * self.radius ** 2)

    def perimeter(self):
        """
        Compute the perimeter (circumference) of the circle
        """
        return abs((self.radius + self.radius) * pi)


class Rectangle(Shape):
    def __init__(self, width, height):
        """
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Compute the area of the rectangle
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        Compute the perimeter of the rectangle
        """
        return (self.width + self.height) * 2


def shape_info(Shape):
    """
    Function that prints the area and perimeter of a given shape
    using duck typing (without checking type explicitly)
    """
    print(f"Area: {Shape.area()}")
    print(f"Perimeter: {Shape.perimeter()}")
