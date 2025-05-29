#!/usr/bin/env python3
"""Custom list class that prints messages on common operations."""


class VerboseList(list):
    """List that prints a message when modified."""

    def append(self, item=None):
        """Add an item and print a message."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items=[]):
        """Add multiple items and print a message."""
        item_count = len(items)
        super().extend(items)
        print("Extended the list with [{}] items.".format(item_count))

    def remove(self, item=None):
        """Remove an item and print a message."""
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, index=-1):
        """Remove and return item at index, print a message."""
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
