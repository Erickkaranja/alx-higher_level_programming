#!/usr/bin/python3
# author: Erick Karanja
'''Defining class square.'''


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

    @property
    def size(self):
        '''gets the value of size.'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''sets the value of size.'''
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        '''prints the square using # characters.'''
        if self.size != 0:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print(" ")
        print(" ")

    def area(self):
        '''computes the area of a square.'''
        return(self.__size * self.__size)
