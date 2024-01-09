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

    def to_json(self):
        """ Get a dict representation of the student """
        return self.__dict__
