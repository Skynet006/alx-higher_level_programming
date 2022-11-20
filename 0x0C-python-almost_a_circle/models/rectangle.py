#!/usr/bin/python3
"""
Module rectangle
Contain class base
With static mthod to_json_string(list_dictionaries),
from_json_string(json_string) and draw(list_rectangles,
list_squares)
with class method save_to_file(cls, list_objs),
create(cls, **dictionary), load_from_file(cls),
load_from_file_csv(cls) and save_to_file_csv(cls, list_objs)
Contain subclass Rectangle
with public insatnce method area, display,
update and to_dictionary
"""

from models.base import Base


class Rectangle(Base):
    """class that represent Rectangle
    that inherits from Base class
    Attributes
    ----------
    width : int
        The width of the rectangle
    height : int
        The height of the rectangle
    x : int
        Varable x
    y : int
        varable y
    id : int
        Identification number
    Method
    ---------
    area(self)
        compute the area of the rectangle
    display(self)
        print the rectangle shape filled with # character
    upate(self, *args, **kwargs)
        assigns an argument to each attribute
    to_dictionary(self):
        reterives the dictionary representation of a Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initalize private width, height, x an y attributes
        Parameters
        ----------
        width : int
            The width of the rectangle
        height : int
            The height of the rectangle
        x : int
            Varable x
        y : int
            varable y
        id : int
            Identification number
        Raises
        ---------
        TypeError
            if the width and height is not integer
            if x and y is not integer
        ValueError
            if width and height is less and equal to zero
            if x and is less than 0
        """

        super().__init__(id)
        if type(width) is int:
            self.__width = width
        else:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is int:
            self.__height = height
        else:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is int:
            self.__x = x
        else:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is int:
            self.__y = y
        else:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

    @property
    def width(self):
        """retrieve prvate width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value to private width attribute
        Parameter
        -----------
        value : int
            the value  of private width attribute
        Raises
        -------
        TypeError
            if the width is not integer
        ValueError
            if width is less and equal to zero
        """
        if type(value) is int:
            self.__width = value
        else:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """retrieve prvate heigth attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the value to private height attribute
        Parameter
        -----------
        value : int
            the value  of private height attribute
        Raises
        -------
        TypeError
            if the height is not integer
        ValueError
            if height is less and equal to zero
        """
        if type(value) is int:
            self.__height = value
        else:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """retrieve prvate x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the value to private x attribute
        Parameter
        -----------
        value : int
            the value  of private x attribute
        Raises
        --------
        ValueError
            if x is less than 0
        TypeError
            if x is not integer
        """
        if type(value) is int:
            self.__x = value
        else:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """retrieve prvate y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the value to private y attribute
        Parameter
        -----------
        value : int
            the value  of private y attribute
        Raises
        --------
        ValueError
            if y is less than 0
        TypeError
            if y is not integer
        """
        if type(value) is int:
            self.__y = value
        else:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """compute the area of the rectangle
        Returns
        -------
        int
            The multiplication of rectangle width and height
        """
        return self.width * self.height

    def display(self):
        """print the rectangle shape filled with # character"""
        msg = [" " * self.x + "#" * self.width for i in range(self.height)]
        print("\n" * self.y + "\n".join(msg))

    def __str__(self):
        """infromal string representation of Rectangle object
        Returns
        --------
        str
          [Rectangle] (<self.id>) <self.x>/<self.y> -
          <self.width>/<self.height>
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
          self.__class__.__name__, self.id, self.x,
          self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        new_value = []
        attr = ["id", "width", "height", "x", "y"]
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
        dic["x"] = self.x
        dic["y"] = self.y
        dic["id"] = self.id
        dic["height"] = self.height
        dic["width"] = self.width
        return dic
