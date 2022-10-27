#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ replaces all occurrences of an element by another in a new list"""
    new_list = []
    for i in range(len(my_list)):
        if my_list[1] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[i])
    return new_list
