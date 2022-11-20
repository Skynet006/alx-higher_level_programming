#!/usr/bin/python3

"""
Module 2-append_write
Contain function that append a string at the end of a text file
Return the number of added character
"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a tetx file
    Return number of character added
    """
    with open(filename, mode='a', encoding='utf-8') as file_name:
        file_name.write(text)
    return len(text)
