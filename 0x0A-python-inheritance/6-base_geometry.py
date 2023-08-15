#!/usr/bin/python3
"""A module that defines a class BaseGeometry.
"""


class BaseGeometry:
    """A class BaseGeometry.

    Methods:
        area: Public instance method that raises an Exception with
        the message "area() is not implemented"
    """

    def area(self):
        """Public instance method that raises and exception.
        """
        raise Exception("area() is not implemented")
