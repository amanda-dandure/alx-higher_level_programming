#!/usr/bin/python3
""" Defining a JSON to object func """
import json


def from_json_string(my_str):
    """ Return the python object representation of a JSON str """
    return json.loads(my_str)
