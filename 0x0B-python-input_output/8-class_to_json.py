#!/usr/bin/python3
# Author: Erick Karanja
'''Defines a python class to a JSON function.'''


def class_to_json(obj):
    '''Returns dict representation of a simple data structure,'''
    return obj.__dict__
