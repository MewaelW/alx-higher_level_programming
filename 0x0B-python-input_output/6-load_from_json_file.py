#!/usr/bin/python3
""" A module which creates an object from JSON file.
"""
import json


def load_from_json_file(filename):
    """ A function which creates an Object from JSON file.

    Arg:
        filename: textfile name

    Raise:
        Exception: when the object can't be encoded

    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
