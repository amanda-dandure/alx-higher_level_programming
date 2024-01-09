#!/usr/bin/python3
""" Defining a class named  student """


class Student:
    """ Representing the student """

    def __init__(self, first_name, last_name, age):
        """ Initializing a new student

        Args:
            first_name (str): This is the first name of the student
            last_name (str): This is the last name of the student
            age (int): This is the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Getting a dict representation of the student

        If attr is a list of str, represents only those attr
        included in the list

        Args:
            attr (list): (Optional) the attr to represent
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """ Replacing all attr of the student

        Args:
            json (dict): This is the key/value pairs to replace attr
        """
        for k, v in json.items():
            setattr(self, k, v)
