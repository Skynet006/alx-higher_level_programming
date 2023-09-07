#!/usr/bin/python3
"""
Function "add-integer" adds integers
it adds two integers together

"""


def add_integer(a, b=98):
    """
    Adds two intergers
    and then Returns the addition of the two ints,
    or an error if a and b are neither integer nor float
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b