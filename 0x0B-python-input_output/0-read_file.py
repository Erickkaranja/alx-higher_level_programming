#!/usr/bin/python3
# Author: Erick Karanja.
'''defining a file reading function.'''


def read_file(filename=""):
    '''Reads a file and prints it to the stdout.

    Args:
        filename(file):The file to read from.
    '''
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
