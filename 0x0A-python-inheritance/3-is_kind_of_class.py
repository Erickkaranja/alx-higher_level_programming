#!/usr/bin/python
# Author : Erick Karanja
'''Defines the is kind of class function.'''


def is_kind_of_class(obj, a_class):
    '''checks if obj is of instance.
    Args:
        obj(any): Object to check type.
        a_class(type): the type of check.

    Returns:
        if is of kind - True otherwise False.
    '''
    if isinstance(obj, a_class):
        return True
    return False
