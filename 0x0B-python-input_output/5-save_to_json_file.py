#!/usr/bin/python3
""" Defining a JSON file writing func """
import json


def save_to_json_file(my_obj, filename):
    """ Writing an object  to a text file using JSON representation """
    wth open(filename, "w") as f:
        json.dump(my_obj, f)
