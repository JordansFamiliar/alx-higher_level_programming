#!/usr/bin/python3
"""A module that defines a function matrix_divided
that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """A function that divides all elements of a
    matrix.

    Args:
        matrix (list of lists): A matrix of integers or floats.
        div (int or float): The divisor.

    Raises:
        TypeError: Raised if matrix does not contain
        integers or floats or if the rows are not of
        equal length or when div is not an integer or
        float.
        ZeroDivisionError: Raised when div is zero.

    Return:
        A new matrix.
    """

    new_matrix = []

    if div is None:
        raise TypeError("div must be a number")
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of"
                        " integers/floats")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of"
                        " integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        new_row = []
        for item in row:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError("matrix must be a matrix (list of lists) of"
                                " integers/floats")
            new_item = item / div
            if isinstance(new_item, float):
                new_row.append(round(new_item, 2))
            else:
                new_row.append(int(new_item))
        new_matrix.append(new_row)

    return new_matrix
