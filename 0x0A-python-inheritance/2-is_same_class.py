#!/usr/bin/python3
# Author :Erick Karanja
'''Defining is same class function.'''


def is_same_class(obj, a_class):
    '''checks for an isinstance relation.

    Args:
        obj(any): The object to be checked.
        a_class(type): family of check of obj.

    Returns:
        if obj is of instance a_class - True.
        otherwise False.
    '''
    if type(obj) == a_class:
        return True
    return False
