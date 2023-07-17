#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for columns in rows:
            if columns == rows[len(rows) - 1]:
                print("{0:d}".format(columns), end='')
            else:
                print("{0:d}".format(columns), end=' ')
        print()
