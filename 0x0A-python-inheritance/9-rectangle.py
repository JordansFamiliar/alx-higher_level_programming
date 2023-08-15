#!/usr/bin/python3
"""A module that defines a subclass Rectangle.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass of BaseGeometry.
    """

    def __init__(self, width, height):
        """Initialises a new rectangle.

        Args:
            width (int): width.
            height (int): height.
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """A method that returns the area of a rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """A method that returns the string representation
        of the rectangle.
        """
        string = "[Rectangle] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
