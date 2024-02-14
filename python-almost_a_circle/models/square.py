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

    @property
    def size(self):
        """
        Return the size of the square using
        the width of the upper class
        """
        return super().width

    @size.setter
    def size(self, size):
        """ Sets the square size """
        self.width = size

    def update(self, *args, **kwargs):
        """
        Assigns argument to each attribute
        """
        if args is not None:
            count = 0
            for arg in args:
                if count == 0:
                    self.id = arg
                if count == 1:
                    self.width = arg
                if count == 2:
                    self.x = arg
                if count == 3:
                    self.y = arg
                count += 1

        for key, elem in kwargs.items():
            if key == "id":
                self.id = elem
            if key == "size":
                self.width = elem
            if key == "x":
                self.x = elem
            if key == "y":
                self.y = elem

    def to_dictionary(self):
        """ Dictionary representation of the Square """
        square_dic = {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
        return square_dic
