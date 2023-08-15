#!/usr/bin/python3
"""A module that defines a function load_from_json_file
"""


import json


def load_from_json_file(filename):
    """A function that creates an object from a json file.

    Args:
        filename (string): name of the file
    """

    with open(filename, "r") as f:
        obj = json.load(f)
        return obj
