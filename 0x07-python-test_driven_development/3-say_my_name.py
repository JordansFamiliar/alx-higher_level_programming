#!/usr/bin/python3
"""A module that defines a function say_my_name
that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """A function that prints My name is <first name>
    <last name>

    Args:
        first_name (str): First name.
        last_name (str, optional): Last name.

    Raises:
        TypeError: Raised if first_name is None or firs_name/
        last_name is not a string.
    """

    if first_name is None:
        raise TypeError("first_name must be a string")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
