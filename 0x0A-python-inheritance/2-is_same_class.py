#!/usr/bin/python3
# Author :Erick Karanja

def is_same_class(obj, a_class):
    '''checks for an isinstance relation'''
    if type(obj) == a_class:
        return True
    return False
