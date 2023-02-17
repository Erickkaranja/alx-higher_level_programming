#!/usr/bin/python3
# Author: Erick Karanja
'''Defining class squares.'''

from models.rectangle import Rectangle

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

    def update(self, *args, **kwargs):
        '''assigns positional atributes to the class.'''
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.size = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k and v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.size, self.x, self.y)
                    else:
                        self.id = v

                elif k == "size":
                    self.size = v

                elif k == "size":
                    self.size = v

                elif k == "x":
                    self.x = v

                elif k == "y":
                    self.y = v
