#!/usr/bin/python3
"""A module that defines a class Rectangle
"""


class Rectangle:
    """A class Rectangle that defines the width
    and height of a rectangle.

    Properties:
        height(int): Private instance attribute.
        width(int): Private instance attribute.

    Raises:
        ValueError: Raises if width or height is
        less than 0.
        TypeError: Raised if width or height is
        not an integer.
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """A property height that returns the value
        of the private attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """A property setter height to set the private
        attribute height to value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """A property width that returns the value
        of the private attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """A property setter that sets the value of
        the private attribute width to value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
