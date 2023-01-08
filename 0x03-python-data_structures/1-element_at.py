#!/usr/bin/python3

def element_at(my_list, idx):
    '''returns value at index of a list'''
    if idx >= 0 and idx <= len(my_list):
        return my_list[idx]
    else:
        return None
