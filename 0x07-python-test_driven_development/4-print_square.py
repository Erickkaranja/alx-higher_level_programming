#!/usr/bin/python3
# Author : Erick Karanja
''' function that prints a square'''

def print_square(size):

    '''prints squares using # characters.
    Args:
        size (int): size of the square to be printed.
    raises:
        TypeError: size must be an integer.
        ValueError: size must be grater than zero.
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print('#', end="") for j in range(size)]
        print("")
