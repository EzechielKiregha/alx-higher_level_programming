#!/usr/bin/python3
"""a module that defines a 'base' class"""

import json
import csv
import turtle


class Base:
    """A base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """the constructor function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """a static method that serializes a dictionary list"""
        if (not list_dictionaries):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """a static method that decodes a json string"""
        if (not json_string):
            return []
        else:
            return json.loads(json_string)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """a static method that draws Rectangles and Squares\
            using the turtle module"""
        turtoise = turtle.Turtle()
        turtoise.screen.bgcolor("#b7312c")
        turtoise.pensize(4)
        turtoise.shape("turtle")

        turtoise.color("#ffb8ff")
        for rect in list_rectangles:
            turtoise.showturtle()
            turtoise.up()
            turtoise.goto(rect.x, rect.y)
            turtoise.down()
            for i in range(2):
                turtoise.forward(rect.width)
                turtoise.left(90)
                turtoise.forward(rect.height)
                turtoise.left(90)
            turtoise.hideturtle()

        turtoise.color("#b5e3d8")
        for sq in list_squares:
            turtoise.showturtle()
            turtoise.up()
            turtoise.goto(sq.x, sq.y)
            turtoise.down()
            for i in range(2):
                turtoise.forward(sq.width)
                turtoise.left(90)
                turtoise.forward(sq.height)
                turtoise.left(90)
            turtoise.hideturtle()

        turtle.exitonclick()

    @classmethod
    def save_to_file(cls, list_objs):
        """a class method that saves a list of objects into a json file"""
        res_file = cls.__name__
        res_file += ".json"
        if not list_objs:
            with open(res_file, mode="w", encoding="utf-8") as file:
                file.write(cls.to_json_string([]))
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            with open(res_file, mode="w", encoding="utf-8") as file:
                file.write(cls.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """a class method that creates a new instance from\
            a dictionary of attributes"""
        new_inst = cls(10, 10)
        new_inst.update(**dictionary)
        return new_inst
    
    @classmethod
    def load_from_file(cls):
        """a class method that returns all instances from a json file"""
        res_file = cls.__name__ + ".json"
        try:
            with open(res_file, mode="r", encoding="utf-8") as file:
                res = file.read()
                res_list = cls.from_json_string(res)
                res_list = [cls.create(**dct) for dct in res_list]
                return res_list
        except FileNotFoundError:
            return []


    @classmethod
    def save_to_file_csv(cls, list_objs):
        """a class method that serializes list_objs and saves to file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                dict_write = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    dict_write.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """a class method that deserializes CSV format from a file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
