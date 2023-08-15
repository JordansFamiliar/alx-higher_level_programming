#!/usr/bin/python3
"""A module that defines a class BaseGeometry.
"""


class BaseGeometry:
    """A class BaseGeometry.

    Methods:
        area (public instance): Raises an exception.
        integer_validator (public instance): validates value.
    """

    def area(self):
        """Method that raises an exception.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A method that validates value.

        Args:
            name (string): Name.
            value (int): An integer.
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
