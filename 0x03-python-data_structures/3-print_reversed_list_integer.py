#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    '''prints item of a list in reverse'''
    if isinstance(my_list, list):
        my_list.reverse()
        for index in my_list:
            print("{:d}".format(index))
