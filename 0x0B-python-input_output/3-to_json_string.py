#!/usr/bin/python3
# Author: Erick Karanja
'''JSON representation of a python object.'''
import json


def to_json_string(my_obj):
    '''returns a json representation of an object.
    Args:
        my_obj(type): object to be represented in json format.
    '''
    return json.dumps(my_obj)
