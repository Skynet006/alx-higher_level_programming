#!/usr/bin/python3
"""
Module square
Contain class base
With static mthod to_json_string(list_dictionaries),
from_json_string(json_string) and draw(list_rectangles,
list_squares)
with class method save_to_file(cls, list_objs),
create(cls, **dictionary), load_from_file(cls),
load_from_file_csv(cls) and save_to_file_csv(cls, list_objs)
Contain parentclass Rectangle
with public insatnce method area, display and update
Contain subclass Square
with public insatnce method update and to_dictionary
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class that represent square and inherits from Rectangle class
    Attributes
    ----------
    size : int
        The side of the square
    x : int
        Varable x
    y : int
        varable y
    id : int
        Identification number
    Methods
    -----------
    update(self, *args, *kwargs)
        assigns an argument to each attribute
    to_dictionary(self)
        reterives dictionary representation of a Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initalize private width, height, x an y attributes from parent class
        Parameters
        ----------
        size : int
            The side of the square
        x : int
            Varable x
        y : int
            varable y
        id : int
            Identification number
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """retrieve the size of the square
        Return
        --------
        int
            the size of the saquare
        """
        return self.width

    @size.setter
    def size(self, value):
        """set the width and height of the square
        Parameter
        ---------
        value : int
            value assigne dto the width and height
        Raises
        ---------
        TypeError
            if the width is not integer
        ValueError
            if the width is less than and equals to zero
        """
        if type(value) is int:
            self.width = value
            self.height = value
        else:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    def __str__(self):
        """informal string representation of Square object"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        new_value = []
        attr = ["id", "size", "x", "y"]
        i = 0
        if args and len(args) != 0:
            for arg in args:
                new_value.append(arg)
            while i < len(new_value):
                setattr(self, attr[i], new_value[i])
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """reterives the dictionary representation of a Rectangle
        Return
        -------
        dict
            the dictionary representation of a Rectangle
        """
        dic = {}
        dic["id"] = self.id
        dic["x"] = self.x
        dic["size"] = self.size
        dic["y"] = self.y
        return dic
