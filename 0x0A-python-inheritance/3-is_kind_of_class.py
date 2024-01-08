#!/usr/bin/python3
""" Defining a class inherited class-checking func """


def is_kind_of_class(obj, a_class):
    """ Chicking if an object is an instance or inherited instance of a class

    Args:
        obj (any): This is the object to check
        a_class (type): This is the class to match the type of object
    Returns:
        If obj is an instance or inherited instance of a_class - [True]
        Otherwise - [False]
    """
    if isinstance(obj, a_class):
        return True
    return False
