#!/usr/bin/python3
"""module task__01_duck_typing
"""
from math import pi
from abc import ABC, abstractmethod
"""import ABC and abstracmethod from the abc module
and import pi from math
"""


class Shape(ABC):
    """Abstract base class for shapes
    """
    @abstractmethod
    def area(self):
        """abstractmethod must be implemented by subclasses
        """
        pass

    @abstractmethod
    def perimeter(self):
        """abstractmethod to calculate the perimeter of the shape
        """
        pass


class Circle(Shape):
    """Circle class inheriting from Shape
    """
    def __init__(self, radius):
        """initialize a circle with a given radius
        """
        self.radius = radius

    def area(self):
        """get the area of the circle
        """
        return (pi * self.radius ** 2)

    def perimeter(self):
        """get the perimeter of the circle
        """
        return abs((self.radius + self.radius) * pi)


class Rectangle(Shape):
    def __init__(self, width, height):
        """initializes height and width
        """
        self.width = width
        self.height = height

    def area(self):
        """get the area of the Rectangle
        """
        return (self.width * self.height)

    def perimeter(self):
        """get the perimeter
        """
        return (self.width + self.height) * 2


def shape_info(Shape):
    print(f"Area: {Shape.area()}")
    print(f"Perimeter: {Shape.perimeter()}")
