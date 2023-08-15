#!/usr/bin/python3
"""A module that defines a function write_file.
"""


def write_file(filename="", text=""):
    """A function that writes a string to a text file (UTF8)
    and returns the number of characters written.

    Args:
        filename (string): Name of the file.
        text (string): Text to be written.

    Return:
        (int): Number of characters written.
    """

    with open(filename, "w", encoding="utf-8") as f:
        data_written = f.write(text)
        return data_written
