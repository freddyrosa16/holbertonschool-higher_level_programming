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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This function returns a JSON string representation of
        the dictionary.
        """
        if list_dictionaries == None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs
        to a file
        """
        filename = cls.__name__ + '.json'
        with open(filename, 'w') as fd:
            list_instance = []
            if list_objs is None:
                fd.write(cls.to_json_string(list_instance))
            else:
                for i in list_objs:
                    list_instance.append(i.to_dictionary())
                fd.write(cls.to_json_string(list_instance))

    @staticmethod
    def from_json_string(json_string):
        """
        Return a list of JSON string representation.
        """
        if json_string == None:
            return []
        else:
            li = json.loads(json_string)
            return li

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance with all attributes.
        """
        if cls.__name__ == 'Square':
            dummy = cls(5)
        elif cls.__name__ == 'Rectangle':
            dummy = cls(5, 5)
        cls.update(dummy, **dictionary)
        return dummy
