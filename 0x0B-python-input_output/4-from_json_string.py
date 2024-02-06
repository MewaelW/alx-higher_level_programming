#!/usr/bin/python3
"""A module which contains a function that returns an object by
 JSON representation
"""
import json


def from_json_string(my_str):
    """A function which returns an object by a JSON representation

    Arg:
        my_str: JSON representation

    Raise:
        Exception: when the string can't be decoded

    """
    return json.loads(my_str)
