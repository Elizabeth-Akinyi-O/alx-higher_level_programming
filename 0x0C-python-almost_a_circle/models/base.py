#!/usr/bin/python3
"""Defines class base model"""
import json
import csv
import turtle


class Base:
    """Represents the class base for all the other classes

    Attributes:
        __nb_objects (int): Number of Base instances
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialises a new Base

        Args:
            id (int): New Base identity
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries
            (serialization)

        Args:
        list_dictionaries (list): A list of dictionaries
        """

        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): List of instances who inherits of Base
        """

        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string
            (deserialization)

        Args:
            json_string (str): String representing a list of dictionaries
        """

        if json_string is None or json_string == "[]":
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set

        Args:
            **dictionary (dict): double pointer to a dictionary
        """

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return (new)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances depending on cls
            (current class using this method)

        Reads from <cls.__name__>.json
        Args:
            cls: current class using this method

        Returns:
            Empty list - if the file does not exist,
            list of instances - otherwise
        """

        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return ([cls.create(**d) for d in list_dicts])
        except IOError:
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV

        Args:
            list_objs (list): List of inherited Base inheritances
        """

        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                writer = csv.DictWriter(csvfile, field_names=field_names)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in CSV

        Reads from <cls.__name__>.csv

        Returns:
            Empty list - if the file does not exist,
            list of instances - otherwise
        """

        filename = str(cls.__name__) + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, field_names=field_names)
                list_dicts = [dict([key, int(val)] for key, val in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return ([])

    @classmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares using the
             Turtle graphics module

        Args:
            list_rectangles (list): List of Rectangle objects to draw
            list_squares (list): List of Square objects to draw
        """

        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for a in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color
        for sq in list_squares:
            turt.showturtle()
            turt.up
            turt.goto(sq.x, sq.y)
            turt.down()
            for a in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
