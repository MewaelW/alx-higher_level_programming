#!/usr/bin/python3
""" Module which contains a function that appends to a text file
"""


def append_write(filename="", text=""):
    """ Function which appends to a text file

    Arg:
        filename: filename
        text: text to write

    Raise
        Exception: when the file can be opened

    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
