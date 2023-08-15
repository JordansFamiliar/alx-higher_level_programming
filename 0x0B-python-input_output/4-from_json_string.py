#!/usr/bin/python3
"""A module that defines a function from_json_string
"""


import json


def from_json_string(my_str):
    """a function that returns an object (Python data
    structure represented by a JSON string.

    Args:
        my_str (string): an object in json.

    Return:
        (obj): Python object.
    """

    return (json.loads(my_str))
