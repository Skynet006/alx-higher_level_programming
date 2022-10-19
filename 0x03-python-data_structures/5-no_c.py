#!/usr/bin/env python3
def no_c(my_string):
    """ function that removes all characters c and C from a string."""
    length = len(my_string)
    x = 0
    new_string = my_string[:]
    for y in range(length):
        if (my_string[y] == 'c' or my_string[y] == 'c'):
            new_string = new_string[:(y - x)] + my_string[(y + 1):]
            x += 1
    return (new_string)
