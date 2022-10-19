#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position."""
    if idx < 0:
        return (my_list)
    length = len(my_list -1)
    if idx > length - 1:
        return (my_list)
    my_list[idx] = element
    return (my_list)

