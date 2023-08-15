#!/usr/bin/python3
"""A module that defines a function class_to_json.
"""


def class_to_json(obj):
    """A function that returns the dictionary description with
    simple data structure for JSON serialisation of an object.

    Args:
        obj: An instance of a class

    Return:
        (dict): dictionary
    """

    return obj.__dict__
