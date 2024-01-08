#!/usr/bin/python3
""" Defining a class inherited class-checking func """


def inherits_from(obj, a_class):
    """ Checking if an object is an inherited instance of a class

    Args:
        obj (any): This is the object to check
        a_class (type): This is the class to match the type of object
    Returns:
        If obj is an instance or inherited instance of a_class - [True]
        Otherwise - [False]
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
