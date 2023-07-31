#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    counter = 0
    while i < x:
        try:
            my_list[i]
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end='')
                counter += 1
            i += 1
        except ValueError:
            break
    if i > 0:
        print()
    return (counter)
