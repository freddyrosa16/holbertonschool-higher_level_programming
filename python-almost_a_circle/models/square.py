#!/usr/bin/python3
"""
This module contains the class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square that inherit from Rectangle
    it receive width, height, x, y and id from Base
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        When initialise she validates value and then
        proceed to assign them.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns [Square] (id) x/y - size """
        return (f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}')