#!/usr/bin/python3
"""  This Module defines a class for a Rectangle"""


class Rectangle():
    """ Define Class Rectangle

    Attributs:
    width (int): width of Rectangle
    height (int): Height of Rectangle

    """

    def __init__(self, width=0, height=0):
        """
        Initialize width and height of Rectangle

        Args:
        width (int): width of Rectangle
        height (int): Height of Rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of a Rectangle

        Return:
        width of the Rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Define the width of the rectangle

        Args:
            value (int): value for the width rectangle

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Get the height of the Rectangle

        Return:
            Height of the Rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Define the height of the Rectangle

        Args:
            value(int): height of the rectangle

        Raises:
            Typerror: height must be an integer
            ValueError: height must be >= 0
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
