#!/usr/bin/pthon3
# Author: Erick Karanja.
'''writes an Object to a text file, using a JSON representation'''
import json


def save_to_json_file(my_obj, filename):
    '''write an object to a text file using json representation.
    Args:
        my_obj(text): object to be written.
        filename(file): The file to be written to.
    '''
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
