#!/usr/bin/python3
"""
module task__00_abc
"""

from abc import ABC, abstractmethod
"""
import ABC and abstracmethod from the abc module
"""


class Animal(ABC):
    """
    class Animal with an abstract method
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses
        """
        pass


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"
