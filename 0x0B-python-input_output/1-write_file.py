#!/usr/bin/python3
""" Defining a file writing function """


def write_file(filename="", text=""):
    """ Writing a str to a UTF8 text file

    Args:
        filename (str): This is the name of the file to write to
        text (tr): This is the text to write to the file
    Returns:
        The num of char written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
