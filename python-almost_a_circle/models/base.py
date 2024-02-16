#!/usr/bin/python3
"""
This module contains the class Base.
"""


import json


class Base:
    """
    This class will be the base of all other
    classes in this projects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This function initialize the
        class by receiving the id argument
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        This function returns a JSON string representation of
        the dictionary.
        """
        if list_dictionaries == None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
