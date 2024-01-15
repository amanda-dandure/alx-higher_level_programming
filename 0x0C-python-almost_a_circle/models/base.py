#!/usr/bin/python3

""" Defining the Base Model Class """
import json
import csv
import turtle


class Base:
    """ Base Model

    Represents the "base" for all the other classes in project 0x0C

    Private Class Attributes:
        __nb_object (int): number of instantiated bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing a new base

        Args:
            id (int): This is the identity of the new base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON serialization of a list of dicts

        Args:
            list_dictionaries (list): This is a list of dicts.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """ Writing JSON serialization of a list of obj to a file

        Args:
            list_objs (list): This is a list of inherited base instances
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
        """ Returns deserialization of a JSON str

        Args:
            json_string (str): This is a JSON str representation of a list of dicts
        Returns:
            If json_string is None/Empty - [an empty list]
            Otherwise - [the Python list represented by json_string]
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """ Returns a class instance from a dict of attr

        Args:
            **dictionary (dict): Key/Value pairs of attr to be initialized
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
        
    @classmethod
    def load_from_file(cls):
        """ Returns a list of class instances from a file of JSON str

        Reading from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - [an empty list]
            Otherwise - [a list of class instances]
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
        
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Writing the CSV serialization of a list of obj to a file

        Args:
            list_objs (list): This is a list of inherited base instances
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Return a list of class instances from a CSV file

        Reading from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - [an empty list]
            Otherwise - [a list of instantiated classes]
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
    
    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Drawing rectangles and squares using the turtle module

        Args:
            list_rectangles (list): This is a list of rectangle obj to draw
            list_squares (list): This is a list of square objects to draw
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
            for p in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for p in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()


