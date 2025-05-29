#!/usr/bin/python3
"""module abstract class
"""


from abc import ABC, abstractmethod
"""import ABC and abstractmethod from abs module
"""


class Animal(ABC):
    """
    """

    @abstractmethod
    def sound(self):
        """
        """
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"