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

    Methods:
        area: A method that returns the area of a
        rectangle.
        perimeter: A method that returns the perimeter
        of a rectangle.
        __str__: A method that returns a string representation
        using the # character.
        __repr__: A method that returns a string representation
        of the rectangle enabling the creation of a new instance.
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

    def area(self):
        """An instance method area that returns the area
        of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """An instance method perimeter that returns the
        perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """A method __str__ that returns a string
        representation of the rectangle.
        """
        rect = ""
        if self.__width == 0:
            return rect
        for rows in range(self.__height):
            for colummns in range(self.__width):
                rect += '#'
            if rows < self.__height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        """A method __repr__ that returns a string representation
        of the rectangle to be able to recreate a new instance.
        """
        return "Rectangle(" + str(self.__width) + "," + str(self.__height) + ")"
