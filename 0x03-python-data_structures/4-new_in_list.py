#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    '''replacing value at a given index'''
    new_list = my_list.copy()
    if idx >= 0 and idx <= len(new_list) - 1:
        new_list[idx] = element
        return new_list
    else:
        return my_list
