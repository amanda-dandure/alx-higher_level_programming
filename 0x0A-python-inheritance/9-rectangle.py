#!/usr/bin/python3
""" Defining a class Rectangle the inherits from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Initializing a new rectangle

    Args:
        width (int): This is the width of the new rectangle
        height (int): This is the height of the new rectangle
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Returns the area of the Rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Returns the print() & the str() representation of a rectangle """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
