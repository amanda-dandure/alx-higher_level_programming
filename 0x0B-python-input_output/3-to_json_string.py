#!/usr/bin/python3
""" Defining a string to JSON func """
import json


def to_json_string(my_obj):
    """ eturns the JSON representation of a str object """
    return json.dumps(my_obj)
