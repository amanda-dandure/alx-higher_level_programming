#!/usr/bin/python3
""" Containing the MyList class """


class MyList(list):
    """ This is the subclass of list """
    def __init__(self):
        """ This initializes the object """
        super().__init__()

    def print_sorted(self):
        """ This prints the sorted list """
        print(sorted(self))
