#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    '''prints x elements of a list'''
    count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end = "")
            count += 1
        except IndexError:
            break
    print("")
    return count
