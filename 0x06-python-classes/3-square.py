#!/usr/bin/python3
"""A module that contains the definition of a class Square.
"""


class Square:
    """A class represeenting a square shape.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Constructor to initialise the Square obj.
        are(self): Method taht calculates the are of a square.
    """
    def __init__(self, size=0):
        """Constructor for the Square class.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is a negative value.

        Note:
            The __size attribute is a private attribute that stores
            the size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """A method that returns the area of a Square.

        Returns:
            The area of the square.
        """
        return(self.__size * self.__size)
