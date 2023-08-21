#!/usr/bin/python3
"""A module that defines a subclass Rectangle.
"""
from .base import Base


class Rectangle(Base):
    """A subclass that inherits from Base.

    Methods:
        area
        display
        update
        to_dictionary
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Property to get the width.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """Property to set the width.

        Args:
            value(int): the new width.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to zero
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Property to get the height.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """Property to set the height.

        Args:
            value(int): the new height.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to zero.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Property to get x.
        """

        return self.__x

    @x.setter
    def x(self, value):
        """Property to set x.

        Args:
            value(int): value of x.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is under 0.
        """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Poperty to get y.
        """

        return self.__y

    @y.setter
    def y(self, value):
        """Property to set y.

        Args:
            value(int): new value

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is under 0.
        """

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """A method that returns the area value of the
        Rectangle instance.
        """

        return self.width * self.height

    def display(self):
        """A method that prints in stdout the Rectangle
        instance with the character #.
        """

        for i in range(self.y):
            print()
        for row in range(self.height):
            for i in range(self.x):
                print(" ", end="")
            for col in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """A method that returns the string representation
        of the rectangle.
        """

        string = "[Rectangle] "
        string += "(" + str(self.id) + ") " + str(self.x) + "/"\
            + str(self.y) + " - " + str(self.width) + "/"\
            + str(self.height)
        return string

    def update(self, *args, **kwargs):
        """A method that assigns an argument to each attribute.

        Args:
            args (tuple): list of arguments
        """

        att_list = ['id', 'width', 'height', 'x', 'y']
        if len(args) != 0:
            for i in range(len(args)):
                if i < len(att_list):
                    setattr(self, att_list[i], args[i])
                else:
                    break
        else:
            for key, value in kwargs.items():
                if key in att_list:
                    setattr(self, key, value)

    def to_dictionary(self):
        """A method that returns the dictionary representation
        of a rectangle.
        """

        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
