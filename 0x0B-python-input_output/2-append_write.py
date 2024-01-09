#!/usr/bin/python3
""" Defining a file writing function """


def append_write(filename="", text=""):
    """ Appending a str to the end of a UTF8 text file

    Args:
        filename (str): This is the name of the file to write to
        text (tr): This is the text to write to the file
    Returns:
        The num of char written
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
