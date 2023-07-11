#!/usr/bin/python3
def pow(a, b):
    if not(isinstance(a, int) and isinstance(b, int)):
        return None
    else:
        result = a ** b
        return result
