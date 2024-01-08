#!/usr/bin/python3
""" Defining a func that adds attr to objects """


def add_attribute(obj, att, value):
    """ Adding a new attr to an object if possible

    Args:
        obj (any): This is the object to add an attr to
        att (str): This is the name of the attr to add to object
        value (any): This is the value of the attr
    Raises:
        TypeError: If the attr cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
