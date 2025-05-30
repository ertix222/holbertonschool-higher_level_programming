#!/usr/bin/python3
"""module VerboList
"""


class VerboseList(list):
    """list that print message on modification
    """
    def append(self, item):
        """add an item to the list
        """
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """extends the list by adding multiple items
        """
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items.")

    def remove(self, item):
        """removes the first occurrence of the specified item from the list
        """
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """removes and returns the item at the specified index
        """
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item
