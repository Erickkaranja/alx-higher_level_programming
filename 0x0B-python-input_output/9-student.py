#!/usr/bin/python3
# Author: Erick Karanja
'''Defining class students.'''


class Student:
    '''initiliazing class students.'''

    def __init__(self, first_name, last_name, age):
        '''initializes class student object.
        Args:
            first_name (str): students first name.
            last_name (str): student last name.
            age (int): age of the student.
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Returns json representation of class student object.'''
        return self.__dict__
