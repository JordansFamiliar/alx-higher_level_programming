#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    result = add(a, b)
    print("{0:d} + {1:d} = {2:d}".format(a, b, result))
    result = sub(a, b)
    print("{0:d} - {1:d} = {2:d}".format(a, b, result))
    result = mul(a, b)
    print("{0:d} * {1:d} = {2:d}".format(a, b, result))
    result = div(a, b)
    print("{0:d} / {1:d} = {2:d}".format(a, b, result))
