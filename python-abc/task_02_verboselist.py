#!/usr/bin/python3
"""
module task__02_verboselist
"""
from abc import ABC, abstractmethod
"""
import ABC and abstracmethod from the abc module
"""


class VerboseList(list):
    """
    """
    def append(self, item):
        """
        Adds an item to the list
        """
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """
        Extends the list by adding multiple items
        """
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items.")

    def remove(self, item):
        """
        Removes the first occurrence of the specified item from the list
        """
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Removes and returns the item at the specified index
        """
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item