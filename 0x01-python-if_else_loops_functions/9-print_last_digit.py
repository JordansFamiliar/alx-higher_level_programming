#!/usr/bin/python3
def print_last_digit(number):
    result = number % 10
    if number < 0:
        result = -(number) % 10
    return result
