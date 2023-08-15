#!/usr/bin/python3
"""A module that defines a function is_same_class
"""


def is_same_class(obj, a_class):
    """A function that returns True if the object is
    exactly an instance of the specifiied class otherwise
    False.

    Args:
        obj: an object
        a_class: a class

    Return:
        True if object is an instance of class.
        False otherwise.
    """

    return type(obj) is a_class
