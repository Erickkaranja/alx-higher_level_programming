#!/usr/bin/python3
# Author :Erick Karanja
'''This class will be the “base” of all other classes in this project.

Description:
    The goal of it is to manage id attribute in all your future\
    classes and to avoid duplicating the same code (by extension, same bugs).
'''
import json

class Base:
    '''Defining class base.
    Attributes(int): attributes to the base class.
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''constructor to class base.'''
        self.id = id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON representation of list_dictionaries.
        Args:
            list_dictionaries(dict): dictionary to be represented in JSON\
            notation.
        '''
        if list_dictionaries is None or list_dictonaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON representation of list_objs to a file.
        Args:
            list_objs(list): list inherited base instances.
        '''

        filename = cls.__name__ + ".json"

        with open(filename, "w") as jsonfile:
            if (list_objs is None):
                jsonfile.write("[]")

            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of JSON string representation.
        Args:
            json_string(str): A json str representation of a list of dicts.
        Returns:
            if json_string is None or is empty, returns an empty list.
            else python list represented by json_string.
        '''
        if json_sting is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set.'''
