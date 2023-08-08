#!/usr/bin/python3
"""A module that defines a function print_square
that prints a square.
"""


def print_square(size):
    """A function that prints a square with the '#'
    character.

    Args:
        size (int): The length of the square.

    Raises:
        TypeError: Raised if size is not an integer or
        less than zero.
    """

    if size is None or not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for rows in range(size):
        for columns in range(size):
            print('#', end='')
        print()
