#!/usr/bin/python3
"""A module which writes an object to a text file using
 JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """A function which writes an object to a text file
    by JSON representation

    Arg:
        my_obj: object
        filename: textfile name

    Raise:
        Exception: when the object can't be encoded

    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
