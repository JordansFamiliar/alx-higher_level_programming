#!/usr/bin/python3
"""A module that defines  function save_to_json_file.
"""


import json


def save_to_json_file(my_obj, filename):
    """A function that writes an object to a text file using
    json representation.

    Args:
        my_obj (obj): python object.
        filename(str): name of the file.
    """

    with open(filename, "w") as f:
        json.dump(my_obj, f)
