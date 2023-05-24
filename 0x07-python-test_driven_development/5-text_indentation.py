#!/usr/bin/python3
# Author: Erick Karanja.
'''function thatidents a text.'''

def text_indentation(text):
    '''identing text.
    Args:
        text (string): The text to be idented.
    raises:
        TypeError: if text is not a string.
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
