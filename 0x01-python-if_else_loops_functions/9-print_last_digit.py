#!/usr/bin/python3
def print_last_digit(number):
    if isinstance(number, int):
        if number < 0:
            result = -(number) % 10
            return result
        else:
            result = number % 10
            return result
    else:
        return None
