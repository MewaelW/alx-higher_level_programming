#!/usr/bin/python3
""" A module which contains a function that returns the JSON
representation of an object
"""
import json


def to_json_string(my_obj):
    """A function which returns the JSON representation of an object.

    Arg:
        my_obj: object

    Raise:
        Exception: when the object can't be encoded

    """
    return json.dumps(my_obj)
