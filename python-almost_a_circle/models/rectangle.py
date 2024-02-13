#!/usr/bin/python3
"""
This module contains the class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle that inherit from base
    it receive width, height, x, y and id
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        When initialize it will assign the values to it.
        """
        super().__init__(id)

        self.__width = width
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = width

        self.__height = height
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.height = height

        self.__x = x
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be > 0")
        else:
            self.x = x

        self.__y = y
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be > 0")
        else:
            self.y = y

    @property
    def width(self):
        """ Return the width of the Rectangle """
        return self.__width

    @width.setter
    def width(self, width):
        """ Sets the width of the Rectangle """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = width

    @property
    def height(self):
        """ Return the height of the Rectangle """
        return self.__height

    @height.setter
    def height(self, height):
        """ Sets the height of the Rectangle """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.height = height

    @property
    def x(self):
        """ Returns the x of the Rectangle """
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be > 0")
        else:
            self.x = x

    @property
    def y(self):
        """ Returns the y of the Rectangle """
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be > 0")
        else:
            self.y = y
