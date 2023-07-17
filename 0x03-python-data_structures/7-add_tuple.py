#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    num1 = (tuple_a + (0, 0))[0] + (tuple_b + (0, 0))[0]
    num2 = (tuple_a + (0, 0))[1] + (tuple_b + (0, 0))[1]
    tuple_c = (num1, num2)
    return (tuple_c)
