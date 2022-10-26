#!/usr/bin/python3
"""Contains Node and SinglyLinkedList classes"""


class Node:
    """Defines a node of a singly linked list
    """

    def __init__(self, data, next_node=None):
        """Class constructor for Node class"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Getter for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data"""
        if not isinstance(value, int):
            raise Exception("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """Getter for next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for next_node"""
        if value is not None:
            raise Exception("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList class definition"""

    def __init__(self, head=None):
        """Class constructor for SinglyLinkedList class"""
        self.__head = head

    def sorted_insert(self, value):
        """Inserts a new node in a sorted list"""
        self.__head = Node.next_node(value)
