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
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Return the width of the Rectangle """
        return self.__width

    @width.setter
    def width(self, width):
        """ Sets the width of the Rectangle """
        self.__width = width

    @property
    def height(self):
        """ Return the height of the Rectangle """
        return self.__height

    @height.setter
    def height(self, height):
        """ Sets the height of the Rectangle """
        self.__height = height

    @property
    def x(self):
        """ Returns the x of the Rectangle """
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        """ Returns the y of the Rectangle """
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
