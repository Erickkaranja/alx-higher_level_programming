#!/usr/bin/python3

def find_peak(list_of_integers):
    if len(list_of_integers) != 0:
        sorted_numbers = sorted(list_of_integers, reverse=True)
        return sorted_numbers[0]
    return None
