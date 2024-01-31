#!/usr/bin/python3
'''Class defines square'''


class Square:
    '''Class that defines a square'''

    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''Return current square area'''
        return self.__size**2

    @property
    def size(self):
        '''Getter method'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter method'''
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
