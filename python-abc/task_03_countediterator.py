#!/usr/bin/python3


class CountedIterator:
    """Iterator that counts how many items have been returned."""

    def __init__(self, obj):
        self.obj = iter(obj)
        self.counter = 0

    def __next__(self):
        try:
            next_item = next(self.obj)
            self.counter += 1
            return next_item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Return the number of items returned so far."""
        return self.counter
