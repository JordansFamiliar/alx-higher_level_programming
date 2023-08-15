#!/usr/bin/python3
"""A module that defines a subclass MyList that inherits from list.
"""


class MyList(list):
    """A subclass that inherits from list.

    Methods:
        print_sorted: A method that prints a list in ascending order.
    """

    def print_sorted(self):
        """A method that prints a list in ascending order.
        """
        print(sorted(self))
