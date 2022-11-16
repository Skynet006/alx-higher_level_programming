#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    z = 0    
    for elm in range(x):
        try:
            print(my_list[elm], end='')
            z += 1
        except Exception:
            break
        print()
        return z
