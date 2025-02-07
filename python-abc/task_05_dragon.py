#!/usr/bin/python3
"""
module task_05_dragon
"""
from abc import abstractmethod


class SwimMixin:
    """
    Class swim for the creature
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    Class fly for the creature
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A dragon class
    """
    def roar(self):
        print("The dragon roars!")
