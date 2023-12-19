#!/usr/bin/python3
"""Defining the Class Square"""


class Square:
    """Stands as a Square
    Attr:
        __size (int): The size of the side of the Square
    """
    def __init__(self, size=0):
        """Initialize the Square
        Args:
            size (int): The size of the side of the square
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
