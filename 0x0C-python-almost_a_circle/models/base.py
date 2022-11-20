#!/usr/bin/python3
"""
Module base
Contain class base
With static mthod to_json_string(list_dictionaries),
from_json_string(json_string) and draw(list_rectangles,
list_squares)
with class method save_to_file(cls, list_objs),
create(cls, **dictionary), load_from_file(cls),
load_from_file_csv(cls) and save_to_file_csv(cls, list_objs)
"""

import json
import csv
import turtle


class Base:
    """class that represent Base
    Attributes
    ----------
    __nb__objects : int
        Number of object created
    id : int
        Identification number
    Methods
    --------
    to_json_string(list_dictionaries):
        reterive a string representin json object from an object
    save_to_file(cls, list_objs):
        Save json strings of all instances into file
    from_json_string(json_string):
        Reterive Python obj of JSON string representation
    create(cls, **dictionary):
        Reterive an instance with all attributes already set
    load_from_file(cls):
        Retrieve a list of instances:
    save_to_file_csv(cls, list_objs):
        Write the CSV serialization of a list of objects to a file
    load_from_file_csv(cls):
        Retrieve a list of classes instantiated from a CSV file
    draw(list_rectangles, list_squares):
        Draw Rectangles and Squares using the turtle module
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize attribute id
        Parameters
        ----------
        __nb__objects : int
            Number of object created
        id : int
            Identification number
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """reterive a string represention json object from an object
        Parameter
        --------
        list_dictionaries : list
            list of object dictionary
        Returns
        ------------
        str
            "[]" if list_dictionaries is None or empty
            json string represenattion
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save json strings of all instances into file"""
        obj = []
        if list_objs is not None:
            for objs in list_objs:
                obj.append(cls.to_dictionary(objs))
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(obj))

    @staticmethod
    def from_json_string(json_string):
        """Reterive Python obj of JSON string representation
        Parameter
        ----------
        json_string : list
            List of dictionary of json string representation
        Return
        --------
        list
            list of object dictionary reprsentation
        """
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Reterive an instance with all attributes already set
        Parameters
        -----------
        dictionary : dict
            A dictionary contain the attributes name and value
        Return
        -------
        object
            an instance with all attributes
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Retrieve a list of instances:
        Return
        ------
        list
            list of instance
        """
        filename = cls.__name__ + ".json"
        list_obj = []
        try:
            with open(filename, 'r') as f:
                datas = cls.from_json_string(f.read())
            for i, dic in enumerate(datas):
                list_obj.append(cls.create(**datas[i]))
        except IOError:
            pass
        return list_obj

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file
        Parameter
        -----------
        list_objs (list): list
                A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for o in list_objs:
                if cls.__name__ == "Rectangle":
                    csv_writer.writerow([o.id, o.width, o.height, o.x, o.y])
                if cls.__name__ == "Square":
                    csv_writer.writerow([o.id, o.size, o.x, o.y])

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Returns:
        --------
        list
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dic = {"id": int(row[0]),
                           "width": int(row[1]),
                           "height": int(row[2]),
                           "x": int(row[3]),
                           "y": int(row[4])}
                if cls.__name__ == "Square":
                    dic = {"id": int(row[0]),
                           "size": int(row[1]),
                           "x": int(row[2]),
                           "y": int(row[3])}
                o = cls.create(**dic)
                objs.append(o)
        return objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module
        Parameter
        -----------
        list_rectangles : list
            A list of Rectangle objects to draw.
        list_squares : list
            A list of Square objects to draw.
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
            for i in range(2):
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
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
