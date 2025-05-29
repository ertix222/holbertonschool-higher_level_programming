#!/usr/bin/python3
"""module abstract class
"""


from abc import ABC, abstractmethod
"""import ABC and abstractmethod from abs module
"""


class Animal(ABC):
    """class Animal that inherit from ABC
    """

    @abstractmethod
    def sound(self):
        """abstractmethod sound of the class Animal
        """
        pass


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"
