#!/usr/bin/python3
"""A module that defines a class Student.
"""


class Student:
    """A class that defines a student.

    Attributes:
        first_name
        last_name
        age

    Methods:
        to_json
    """

    def __init__(self, first_name, last_name, age):
        """A method that initialises an object of
        Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """A method that returns a dictionary representation
        of a Student.
        """
        return self.__dict__
