#!/usr/bin/python3
# Author: Erick Karanja
'''returns a python object represented by a JSON string'''
import json


def from_json_string(my_str):
    '''defines python object from json object.
    Args:
        my_str(json): string to convert.
    '''
    return json.loads(my_str)
