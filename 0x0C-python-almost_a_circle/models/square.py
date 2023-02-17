#!/usr/bin/python3
# Author: Erick Karanja
'''Defining class squares.'''

import rectangle from model

class Square(Rectangle):
    '''initializing class square.
    Args:
        self (int): value of both width and height of the square.
        x (int): x co-ordinate value.
        y (int): y co-ordinate value.
        id (int): id to the respective square.
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''constructor to the class square.'''
        super.__init__(size, size, x, y, id)

    @property
    def size(self):
        '''Gets the size value to the square.'''
        return (self.__width)

    @size.setter
    def size(self, value):
        '''sets the value of size to the square.'''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value
        self.__height = value

    def to_dictionary(self):
        '''represent dictionary representation to a square.'''
        return {
            "id":self.id
            "size":self.width
            "x":self.x
            "y":self.y

            }
