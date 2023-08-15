#!/usr/bin/python3
"""A module that defines a function inherits_from.
"""


def inherits_from(obj, a_class):
    """A function that returns True if the object is an instance of a
    class that inherited (directly or indirectly) from the specified
    class; otherwise False.

    Args:
        obj: An object.
        a_class: A class.

    Return:
        True or False.
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class
