#!/usr/bin/python3
# Author: Erick Karanja
'''implementing class BaseGeometry.'''


class BaseGeometry:
    '''defining class BaseGeometry.'''

    def area(self):
        '''defines a public class area.'''
        return (width * height)

    def integer_validator(self, name, value):
        '''validates value.'''

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''child class of BaseGeometry.'''

    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self._height = height
