#!/usr/bin/python3
"""
This module have a empty class named Geometry
"""


class BaseGeometry:
    """
    Class description for Base Geometry
    """

    def area(self):
        """
        Public instance method that raise an Exception
        """
        raise Exception('area() is not implemented')

    def integer_validation(self, name, value):
        """
        Public instance method that validates value
        """
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        elif value < 0:
            raise ValueError("<name> must be greater than 0")
        self.name = name
        self.value = value
