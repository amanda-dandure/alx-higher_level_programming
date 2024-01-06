#!/usr/bin/python3
""" Defining a rectangle class """


class Rectangle:
    """ This represents a rectangle """

    def __init__(self, width=0, height=0):
        """ Initializing a brand new rectangle

        Args:
            width (int): This is the width of the new recatngle
            height (int): This is the height of the new rectangle
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """ Get or set the width of the rectangle """
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an int")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """ Get or set the heght of the rectangle """
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an int")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
