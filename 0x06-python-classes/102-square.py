#!/usr/bin/python3
# author: Erick Karanja
'''defining class square.'''


class Square:
    '''initializes a type square'''

    def __init__(self, size=0):
        '''defines a squareby size.
        arg:
        size(int) :size of a square.
        '''
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        '''gets the value of size.'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''sets the value of size.'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        '''Checks for equality.'''
        return self.area() == other.area()

    def __lt__(self, other):
        '''checks the less than operator.'''
        return self.area() < other.area()

    def __gt__(self, other):
        """checks for the greater than operator."""
        return self.area() > other.area()

    def __le__(self, other):
        '''checks for the less than or equal to.'''
        return self.area() <= other.area()

    def __ge__(self, other):
        '''checks for the greater than or equal to operator.'''
        return self.area() >= other.area()

    def __ne__(self, other):
        '''checks for not equal to operator.'''
        return self.area() != other.area()

    def area(self):
        '''computes the area of a square.'''
        return(self.__size * self.__size)
