#!/usr/bin/python3
# Author :Erick Karanja
'''defining MyList class'''


class MyList(list):
    '''sorted list for list built-in'''

    def print_sorted(self):
        '''prints list items but sorted in ascending order.'''
        print(sorted(self))
