#!/usr/bin/python3
""" Defining an empty class named BaseGeometry """


class BaseGeometry:
    """ This represents BaseGeometry """

    def area(self):
        """ This is not implemnented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validating a parameter as an int

        Args:
            name (str): This is the name of the parameter
            value (int): This is the parameter to validate
        Raises:
            TypeError: If value is not an int
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
