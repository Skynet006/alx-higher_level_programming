#!/usr/bin/python3
"""
Module 5-save_to_json
Contain a function that writes an object to a text file
Using a json representation
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using a json representation"""
    with open(filename, 'w') as file_name:
        json.dump(my_obj, file_name)
