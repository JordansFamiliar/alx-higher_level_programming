#!/usr/bin/python3
"""A module that defines a function append_write.
"""


def append_write(filename="", text=""):
    """A function that appends a string at the end of a text file
    (UTF8) and returns the number of characters added.

    Args:
        filename (string): Name of the file.
        text (string): Text to be written.

    Return:
        (int): Number of characters written.
    """

    with open(filename, "a", encoding="utf-8") as f:
        data_written = f.write(text)
        return data_written
