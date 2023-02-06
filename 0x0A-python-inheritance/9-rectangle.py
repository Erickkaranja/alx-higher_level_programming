#!/usr/bin/python3
# Author: Erick Karanja
'''Defines a class rectangle that inherits from BaseGeometry'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''representing rectangle using baseGeometry.'''

    def __init__(self, width, height):
        '''constructor to the class rectangle.
        Args:
            width(int): width to the rectangle.
            height(int): height to the rectangle.
        '''

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        '''Returns the area of a rectangle.'''
        return self.__width * self.__height

    def __str__(self):
        '''Returns the print() and str() representation of a Rectangle.'''
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
