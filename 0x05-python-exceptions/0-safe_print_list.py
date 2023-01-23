#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    '''prints x elements of a list'''
    try:
        for i in range(x - 1):
            print(my_list[i])
    except indexError:
        print(my_list)
