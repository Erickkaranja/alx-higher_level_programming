#!/usr/bin/python3
# Author : Erick Karanja
'''Function that appends text at the end of a file.'''


def append_write(filename="", text=""):
    '''appends text at end of a file.
    Args:
        filename(file): file to be appended to.
        text(str): The string to be appended.
    '''
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
