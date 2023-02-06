#!/usr/bin/python3
# Author: Erick Karanja
'''implementing class BaseGeometry.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''child class of BaseGeometry.'''

    def __init__(self, width, height):
    '''initializes a new rectangle.
    args:
        width(int): width of the rectangle.
        height(int): height of the rectangle.
    '''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self._height = height
