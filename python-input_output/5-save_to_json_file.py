#!/usr/bin/python3
"""
this module contain a function that writes and
object to a text file, using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    this function writes and object to a
    text file, using JSON representation
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
