#!/usr/bin/python3
#0-print_list_integer.py

'''prints all integers in a list'''
def print_list_integer(my_list=[]):
    for index in range(len(my_list)):
        print("{:d}".format(my_list[index]))
