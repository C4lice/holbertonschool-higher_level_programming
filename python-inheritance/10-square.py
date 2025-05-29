#!/usr/bin/python3
"""
Module that creates a Square class based on Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class that defines a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a Square instance with a given size.

        Args:
            size (int): The size of the square's sides.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2
