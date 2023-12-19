#!/usr/bin/python
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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """Calculating the Area of the Square
        Returns:
            The Squares Area
        """
        return (self.__size) ** 2
