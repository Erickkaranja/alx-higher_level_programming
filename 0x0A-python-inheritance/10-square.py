#!/usr/bin/python3
# Author: Erick Karanja
'''parent class to be used by the square method'''
Rectangle = __import__('9-rectangle').Rectangle

'''initializing class Square.'''


class Square(Rectangle):
    '''constructor to class square.'''
    def __init__(self, size):
        '''initializing square variables.
        args:
            size (int): size of the square.
        '''

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
