#!/usr/bin/python3
""" Defining an object attr loookup function """


def lookup(obj):
    """ Returns a list of an objects available attr """
    return (dir(obj))
