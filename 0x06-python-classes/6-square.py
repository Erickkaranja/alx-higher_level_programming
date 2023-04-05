#!/usr/bin/python3
# author: Erick Karanja
'''Defining class square.'''


class Square:
    '''initializes a type square'''
    def __init__(self, size=0, position=(0, 0)):
        '''defines a squareby size.
        arg:
        size(int):size of a square.
        '''

        self.__size = size
        self.__positon = position 

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

    @property
    def position(self):
        '''position getter.'''

        return self.__position

    @position.setter
    def position(self, value):
        '''position setter.'''
        if (type(value) != tuple or len(value)!= 2 or value[0] < 0 or value[1]
                      < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value

    def my_print(self):
        '''prints the square using # characters.'''
        if (self.__size == 0):
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def area(self):
        '''computes the area of a square.'''
        return(self.__size * self.__size)
