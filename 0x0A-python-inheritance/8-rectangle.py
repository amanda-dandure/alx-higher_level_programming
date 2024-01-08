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
