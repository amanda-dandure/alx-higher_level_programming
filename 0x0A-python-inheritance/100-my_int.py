#!/usr/bin/python3
""" Defining a class MyInt that inherits from int """


class MyInt(int):
    """ Inverting in toperators == and != """

    def __eq__(self, value):
        """ Overriding == operator wiht != behavoir """
        return self.real != value

    def __ne__(self, value):
        """ Overriding == operator wiht == behavoir """
        return self.real == value
