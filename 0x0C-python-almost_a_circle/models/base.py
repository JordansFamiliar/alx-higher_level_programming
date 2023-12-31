#!/usr/bin/python3
"""A module that defines a class Base.
"""
import turtle
import csv
import json


class Base:
    """A base class.

    Attributes:
        nb_objects (private, int)

    Methods:
        to_json_string
        save_to_file
        from_json_string
        create
        load_from_file
        save_to_file_csv
        load_from_file_csv
        draw
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor.

        Args:
            id(int, optional)
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation
        of list_dictionaries.
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """A class method that writes the JSON string representation
        of list_objs to a file.
        """

        filename = cls.__name__ + ".json"
        with open(filename, "w+") as f:
            dict_list = [obj.to_dictionary() for obj in list_objs]
            f.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """A method that returns the list of the JSON string
        representation json_string.
        """

        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """A class method that returns an instance with all attributes
        already set.
        """

        class_name = cls.__name__
        new_instance = None
        if class_name == 'Rectangle':
            new_instance = cls(dictionary.get('width'),
                               dictionary.get('height'))
        elif class_name == 'Square':
            new_instance = cls(dictionary.get('size'))
        if new_instance:
            new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """A class method that returns a list of instances.
        """

        obj_list = []
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                json_string = f.read()
                obj_list = cls.from_json_string(json_string)
        except Exception:
            pass
        return [cls.create(**obj) for obj in obj_list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """A class method that serialises in CSV.
        """

        filename = cls.__name__ + ".csv"
        with open(filename, "w+") as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(list(list_objs[0].to_dictionary().keys()))
            for obj in list_objs:
                csvwriter.writerow(list(obj.to_dictionary().values()))

    @classmethod
    def load_from_file_csv(cls):
        """A class method that deserialises in CSV.
        """

        obj_list = []
        csv_data = []
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    for key, value in row.items():
                        row[key] = int(value)
                    csv_data.append(row)
        except Exception:
            pass
        string = cls.to_json_string(csv_data)
        obj_list = cls.from_json_string(string)
        return [cls.create(**obj) for obj in obj_list]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """A method that opens a window and draws all the Rectangles and
        Squares
        """

        t = turtle.Turtle()
        for obj in list_rectangles:
            t.goto(obj.x, obj.y)
            for i in range(2):
                t.forward(obj.height)
                t.right(90)
                t.forward(obj.width)
                t.right(90)
        for obj in list_squares:
            t.goto(obj.x, obj.y)
            for i in range(4):
                t.forward(obj.size)
                t.right(90)
        turtle.bye()
