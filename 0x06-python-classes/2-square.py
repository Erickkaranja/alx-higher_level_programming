#!/usr/bin/python3
# author: Erick Karanja
'''defining class square'''


class Square:
    '''defining class square.'''

    def __init__(self, size=0):
        '''creating the square.

        Args:
            size(int) :defines a square by its size.
        '''
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
