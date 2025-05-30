#!/usr/bin/python3
"""module demonstrating multiple inheritance with animals
"""


class Fish:
    """class representing a fish
    """
    def swim(self):
        """print swimming behavior
        """
        print("The fish is swimming")

    def habitat(self):
        """print fish habitat
        """
        print("The fish lives in water")


class Bird:
    """class representing a bird
    """
    def fly(self):
        """print flying behavior
        """
        print("The bird is flying")

    def habitat(self):
        """print bird habitat
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """class representing a flying fish
    """
    def swim(self):
        """overrides swim for the flying fish
        """
        print("The flying fish is swimming!")

    def fly(self):
        """overrides fly for the flying fish
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """overrides habitat for the flying fish
        """
        print("The flying fish lives both in water and the sky!")
