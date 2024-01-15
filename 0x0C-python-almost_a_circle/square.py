#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Representing a square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializing a new square

        Args:
            size (int): This is the size of the new square
            x (int): This is the x coordinate of the new square
            y (int): This is the y coordinate of the new square
            id (int): This is the identity of the new square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Get/Set the size of the square """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
    
    def update(self, *args, **kwargs):
        """ Updating the square

        Args:
            *args (ints): new attr values
                - 1st arg represents id attr
                - 2nd arg represents size attr
                - 3rd arg represents x attr
                - 4th arg represents y attr
            **kwargs (dict): New key/value pairs of attr
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """ Returns the dict representation of the square """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """ Returns the print() and str() representation of a square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

