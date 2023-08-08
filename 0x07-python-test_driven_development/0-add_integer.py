#!/usr/bin/python3

"""A module containing the definition of a function add_integer
that adds two integers or floats
"""


def add_integer(a, b=98):
    """A function that adds two integers or floats

    Args:
        a (int or float): first number.
        b (int or float, optional): second number.

    Raise:
        TypeError: If a or b is not a float or integer.

    Return:
        int: The addition of a and b.
    """
    if a is None:
        raise TypeError("a must be an integer")
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
