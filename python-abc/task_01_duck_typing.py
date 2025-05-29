#!/usr/bin/python3
"""
Defines an abstract Shape class and two implementations: Circle and Rectangle.
Includes a function to display area and perimeter using duck typing.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        ...

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        ...


class Circle(Shape):
    """Circle shape with radius."""

    def __init__(self, radius):
        """Initialize with radius."""
        self.radius = abs(radius)

    def area(self):
        """Return circle area."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return circle perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape with width and height."""

    def __init__(self, width, height):
        """Initialize with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Return rectangle perimeter."""
        return (2 * self.width) + (2 * self.height)


def shape_info(shape):
    """Print area and perimeter of a shape."""
    area = shape.area()
    perimeter = shape.perimeter()

    print("Area: {}".format(area))
    print("Perimeter: {}".format(perimeter))
