#!/usr/bin/python3
# Author: Erick Karanja
'''Defining an abject attribute lookup function.'''


def lookup(obj):
    '''prints all  list of available attributes and methods of an object.
    args:
    obj (object): object to find attribytes to.
    '''
    return (dir(obj))
