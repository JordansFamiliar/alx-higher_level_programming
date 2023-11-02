#!/usr/bin/python3
"""A module that finds a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
    """
    Find a peak in an unsorted list of integers.

    Args:
        list_of_integers (list of int): The list of unsorted integers.

    Returns:
        int: A peak from the list if found, or None if the list is empty.
    """
    length = len(list_of_integers)
    if length == 0:
        return None
    start, end = 0, length - 1
    while start < end:
        mid = start + (end - start) // 2
        if list_of_integers[mid] > list_of_integers[mid - 1] and list_of_integers[mid] > list_of_integers[mid + 1]:
            return list_of_integers[mid]
        if list_of_integers[mid - 1] > list_of_integers[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return list_of_integers[start]
