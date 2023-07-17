#!/usr/bin/python3
def max_integer(my_list=[]):
    max = None
    if len(my_list) == 0:
        return (None)
    for i in my_list:
        if max is None or i > max:
            max = i
    return (max)
