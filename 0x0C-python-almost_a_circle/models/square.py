#!/usr/bin/python3
"""A module that defines a class Square.
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """A class that defines a square.

    Methods:
        update
        to_dictionary
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for the square instance.
        """

        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        """Getter for size.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size.

        Args:
            value(int): New value of size.
        """

        super(Square, Square).width.fset(self, value)
        self.__height = value
        self.__size = value

    def __str__(self):
        """Prints the string representation of the square.
        """

        string = "[Square] "
        string += "(" + str(self.id) + ") " + str(self.x) + "/"\
            + str(self.y) + " - " + str(self.size)
        return string

    def update(self, *args, **kwargs):
        """A public method that assigns attributes.
        """

        if len(args) > 0:
            new = args[:]
            if len(args) >= 2:
                new = args[0:2] + args[1:]
                self.__size = args[1]
            super().update(*new)
            pass
        if 'size' in kwargs:
            kwargs['width'] = kwargs['size']
            kwargs['height'] = kwargs['size']
            self.__size = kwargs['size']
            kwargs.pop('size')
        super().update(**kwargs)

    def to_dictionary(self):
        """Returns the dictionary representation of
        a square.
        """

        r_dict = super().to_dictionary()
        r_dict['size'] = r_dict['width']
        r_dict.pop('width')
        r_dict.pop('height')
        return r_dict
