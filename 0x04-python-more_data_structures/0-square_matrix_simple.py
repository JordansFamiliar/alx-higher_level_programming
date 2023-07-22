#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[items ** 2 for items in rows] for rows in matrix]
    return (new_matrix)
