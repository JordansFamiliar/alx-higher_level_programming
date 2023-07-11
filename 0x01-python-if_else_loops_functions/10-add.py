#!/usr/bin/python3
def add(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return None
    result = a + b
    return result
