#!/usr/bin/python3
# Author: Erick Karanja
'''defining function add_integer
usage:
     takes first integer add to second integer
     returns val or err.
'''


def add_integer(a, b=98):

    '''args:a(int): first integer of adddition.
           b(int): second integer of addition.
    '''

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
