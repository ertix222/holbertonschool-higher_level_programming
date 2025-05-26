#!/usr/bin/python3

"""
create a class MyList
"""


class MyList(list):
    """
    a class that inherits from list
    with a public instance method
    that print in asc sort
    """
    def print_sorted(self):
        print(sorted(self))
