#!/usr/bin/python3
""" Defining a class checking func """


def is_same_class(obj, a_class):
    """ Chicking is if an object is excatly an instance of a class

    Agrs:
        obj (any): This is the object to check
        a_class (type): This is the class to match the type of obj
    Returns:
        if obj is excatly an instance of a_class - [True]
        Otherwise - [False]
    """
    if type(obj) == a_class:
        return True
    return False
