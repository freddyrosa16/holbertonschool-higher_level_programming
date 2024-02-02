#!/usr/bin/python3
"""
    This module will have a function that will add 2 integers.
    First number will be a and second number passed will be b.
    Returning the addition of both number.
"""


def add_integer(a, b=98):
    """
        Function that adds 2 integers.
        Check if a and b are integers or floats.
        If not a error will be raised.
        Otherwise float will be casted to integer in order to
        recreate add both.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
