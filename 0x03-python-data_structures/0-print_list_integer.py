#!/usr/bin/python3

def print_list_integer(my_list=[]):
    '''prints members of a list'''
    for index in range(len(my_list)):
        print("{:d}".format(my_list[index]))
