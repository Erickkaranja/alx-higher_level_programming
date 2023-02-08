#!/usr/bin/python3
# Author: Erick Karanja
'''Function that inserts a line of text into a file.'''


def append_after(filename="", search_string="", new_string=""):
    '''inserts text after each line containing a given text.
    Args:
        filename(file): The text file to append on.
        search_string(str): The string to be searched.
        new_string(str): The string to be added.
    '''
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w") as w:
        w.write(text)
