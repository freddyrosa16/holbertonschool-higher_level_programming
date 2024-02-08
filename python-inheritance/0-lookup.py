#!/usr/bin/python3
"""
This module contains a function call
lookup that returns a list of available
attributes and method of the pass object
"""


def lookup(obj):
    """
    This function returns a list of available
    attributes and methods of an object
    passed to the function.
    """
    return dir(obj)
