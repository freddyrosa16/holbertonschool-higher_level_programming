#!/usr/bin/python3
"""
This module have a class
that defines a rectangle
"""


class Rectangle:
    """ Definition of rectangle attribute """

    def __init__(self, width=0, height=0):
        self.__height = height
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """ Return the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        """ Return the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the rectangle """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        """ Looks for the area of the rectangle """
        return self.height * self.width

    def perimeter(self):
        """ Looks for the perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.height * 2) + (self.width * 2)

    def __str__(self):
        """ Prints the rectangle shape """
        if self.width == 0 or self.height == 0:
            return ""
        for column in range(self.height):
            for row in range(self.width):
                print("#", end="")
            print()

    def __repr__(self):
        """ String representation of the rectangle """
        return f"({self.width}, {self.height})"
