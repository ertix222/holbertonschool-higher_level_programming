#!/usr/bin/python3
"""
module task_03_ocuntediterator
"""


class CountedIterator():
    """
    Custom iterator that keeps track
    of the number of items iterated.
    """
    def __init__(self, iterable):
        """
        Initializes the CountedIterator with an iterable.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Returns the next item in the iterator and increments the count.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """
        Returns the number of items iterated over
        """
        return self.count
