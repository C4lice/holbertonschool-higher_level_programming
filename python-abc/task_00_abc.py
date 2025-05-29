#!/usr/bin/python3
"""
Module that defines an abstract Animal class and two concrete subclasses: Dog and Cat.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract base class representing an Animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by all subclasses.
        Should return the sound made by the animal.
        """
        pass


class Dog(Animal):
    """
    Dog class that inherits from Animal and implements the sound method.
    """

    def sound(self):
        """
        Return the sound made by a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class that inherits from Animal and implements the sound method.
    """

    def sound(self):
        """
        Return the sound made by a cat.
        """
        return "Meow"


# Example usage
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    print(dog.sound())
    print(cat.sound())
