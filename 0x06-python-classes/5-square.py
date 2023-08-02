#!/usr/bin/python3

class Square:
    """A class representing a square shape.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Constructor to initialize the Square object.
        area(self): Method that calculates the area of a square.
        my_print(self): Method that prints the square in #s.

    Properties:
        size (int): Property to get or set the size of the square.

    Raises:
        TypeError: If the provided size is not an integer.
        ValueError: If the provided size is a negative value.

    Note:
        The __size attribute is a private attribute that stores the size of the
        square.
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

    @property
    def size(self):
        """Property to get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Property to set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is a negative value.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method that returns the area of a Square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Method that prints in stdout the square with the character #
        """
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
        if self.__size == 0:
            print()
