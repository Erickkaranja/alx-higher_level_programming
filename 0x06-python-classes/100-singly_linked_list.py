#!/usr/bin/python3
#Erick Karanja
'''Defining class node.'''


class Node:
    '''initializing class node.'''

    def __init__(self, data, next_node=None):
        '''constructor to class node.'''

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''Data getter.'''
        return self.__data

    @data.setter
    def data(self, value):
        '''Data setter.'''

        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        '''next_node getter.'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''next_node setter.'''
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    '''intializing class SinglyLinkedList.'''

    def __init__(self):
        '''constructor to class.'''
        self.__head = None

    def sorted_insert(self, value):
        '''inserts a new Node into the correct sorted position.

        Description: This node is inserted into the list at the correct
                     ordered position.

        Arg:
            value(node): The new node to be inserted.
        '''
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new

        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new

        else:
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node

            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        '''defines the string representation of a singly linked list.'''
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
