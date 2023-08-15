#!/usr/bin/python3
"""A module that defines a function to_json_string.
"""

import json


def to_json_string(my_obj):
    """A function that returns the JSON representation
    of an object (string).

    Args:
        my_obj (string): an object.

    Return:
        (string): A JSON representation of my_obj.
    """

    return json.dumps(my_obj)
