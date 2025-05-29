#!/usr/bin/python3
"""
module that create a square class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or a subclass of a_class, otherwise False.
    """
    return isinstance(obj, a_class)
