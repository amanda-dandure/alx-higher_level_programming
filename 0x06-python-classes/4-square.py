#!/usr/bin/python3
"""Defining a Square"""


class Square:
    """Representing a Square
    Attr:
        __size (int): The size of the side of the Square
    """
    def __init__(self, size=0):
        """Initializing the Square
        Args:
            size (int): The size of the side of a Square
        Returns:
            Nothing
        """
        self.__size = size

    def area(self):
        """Calculating the Area of the Square
        Returns:
            The Squares Area
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """ The getter of __size
        Returns:
            Size of the Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """The setter of __size
        Args:
            value (int): Size of the side of a Square
        Returns:
            Nothing
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
