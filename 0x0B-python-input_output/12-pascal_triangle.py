#!/usr/bin/python3
"""A module that defines a function pascal_triangle.
"""


def pascal_triangle(n):
    """A function that returns a list of lists of
    integers representing the Pascal's triangle.

    Args:
        n (int): Number

    Return:
        list
    """

    if n <= 0:
        return []
    ret_list = []
    for rows in range(n):
        col = []
        for columns in range(rows + 1):
            value = 0
            if columns == 0 or columns == rows:
                value = 1
            else:
                value = ret_list[rows - 1][columns - 1] + ret_list[rows - 1]\
                    [columns]
            col.append(value)
        ret_list.append(col)
    return ret_list
