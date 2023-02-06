#!/usr/bin/python3
# Author: Erick Karanja
'''Defining class inherit_from.'''


def inherits_from(obj, a_class):
    '''checks if obj is a subclass of a_class.
    Args:
        abj(any): The object of check.
        a_class(type): The class of obj check.

    Returns:
        if issubclass - True otherwise False.
    '''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
