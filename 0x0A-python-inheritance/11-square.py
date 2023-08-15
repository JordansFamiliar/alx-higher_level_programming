#!/usr/bin/python3
"""A module that defines a subclass Square.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that represents a square.
    """

    def __init__(self, size):
        """A method that initialises a Square.

        Args:
            size (int): the size.
        """

        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """A method that returns the string representation
        of the Square.
        """

        string = "[Square]"
        string += str(self.__size) + "/" + str(self.__size)
        return string
