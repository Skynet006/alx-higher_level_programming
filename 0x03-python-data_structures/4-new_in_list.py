#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    replaces an element in a list at a specific position
    without modifying the original list.
    """
    new_list = my_list[:]
    length = len(my_list)
    if idx < 0:
        return (new_list)
    if idx > length - 1:
        return (new_list)
    new_list[idx] = element
    return (new_list)
