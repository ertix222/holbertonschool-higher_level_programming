#!/usr/bin/python3
"""mixin two classes
"""


class SwimMixin:
    """class SwimMixin to mix
    """
    def swim(self):
        """method swim
        """
        print("The creature swims!")


class FlyMixin:
    """class FlyMixin to mix
    """
    def fly(self):
        """method fly
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """class dragon that inheritance
    """
    def roar(self):
        """additional method for the dragon
        """
        print("The dragon roars!")
