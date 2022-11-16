#!/usr/bin/python3
"""
Defines a class Square
"""


class square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square"""
        self.__size = size

    @property
    def size(self):
        """Returns size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size to a value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of a square"""
        sq_area = self.__size ** 2
        return sq_area

