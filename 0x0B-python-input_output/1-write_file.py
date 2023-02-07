#!/usr/bin/python3
# Author: Erick Karanja.
'''Defining a function that writes to a file.'''


def write_file(filename="", text=""):
    '''Writes to a file.

    Args:
        filename(file): the file to be written to.
        text(str): Text to be appended to the file.
    '''
    with open(filename, 'w', encoding="utf-8") as f:
        print(f.write(text))
