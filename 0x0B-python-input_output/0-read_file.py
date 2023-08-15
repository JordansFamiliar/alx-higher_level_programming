#!/usr/bin/python3
"""A module that defines a function read_file.
"""


def read_file(filename=""):
    """A function that reads a text file (UTF8) and
    prints it to stdout.

    Args:
        filename (string): Name of the file.
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
