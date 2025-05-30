#!/usr/bin/python3
"""
module that create a square class
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a subclass of a_class
    (but not a_class itself), otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
