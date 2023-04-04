#!/usr/bin/python3
# author: Erick Karanja

class Square:
    '''initializes a type square'''
    def __init__(self, size=0):
        '''defines a squareby size.
        arg:
        size(int):size of a square.
        '''
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''computes the area of a square.'''
        return(self.__size * self.__size)
