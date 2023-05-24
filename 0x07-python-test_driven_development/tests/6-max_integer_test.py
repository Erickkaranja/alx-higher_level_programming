#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    '''Defines unittests for max_integer([..]).'''

    def test_ordered_list(self):
        '''tests an ordered list.'''
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        '''tests an unordered list.'''
        unordered = [2, 1, 3, 4]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        '''tests a list with the beginning max value.'''
        max_at_beginning = [4, 3, 1, 2]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        '''tests an empty list.'''
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_single_element_list(self):
        '''tests a single element list.'''
        my_list = [4]
        self.assertEqual(max_integer(my_list), 4)

if __name__ == "__main__":
    unittest.main()
