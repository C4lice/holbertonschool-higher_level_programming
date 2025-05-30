#!/usr/bin/python3
"""
Module that creates a BaseGeometry class.
"""


class BaseGeometry:
    """
    Base class for geometry-related operations.
    """

    def area(self):
        """
        Raises:
            Exception: Always raised to indicate that the
            method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is a positive integer.

        Args:
            name (str): The name of the parameter (used in the error message).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
