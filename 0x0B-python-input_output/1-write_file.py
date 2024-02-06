#!/usr/bin/python3
""" Module which contains a function that writes to a text file.
"""


def write_file(filename="", text=""):
    """ Function which writes to a text file

    Arg:
        filename: filename
        text: text to write

    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
