#!/usr/bin/python3
a = 89
b = 10
a, b = (a, b)[1], (a, b)[0]
print("a={:d} - b={:d}".format(a, b))
