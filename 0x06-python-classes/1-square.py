#!/usr/bin/python3
"""This is a Square Class Defination"""


class Square:
    """Stands as a Square
    Attributes:
        __size (int): The sizeof the side of a Square
    """
    def __init__(self, size):
        """Initialize the Square
        Arguements:
            size (int): The size of the side of a Square
        Returns: Nothing
        """
        self.__size = size
