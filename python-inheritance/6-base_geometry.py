#!/usr/bin/python3
"""
module that create a square class
"""


class BaseGeometry:
    """
    Base class for geometry-related operations.
    """

    def area(self):
        """
        Raises an exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")
