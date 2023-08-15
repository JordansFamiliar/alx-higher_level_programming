#!/usr/bin/python3
"""module that defines function lookup.
"""


def lookup(obj):
    """A function that returns a list of available
    attributes and methods of an object.
    """

    return (dir(obj))
