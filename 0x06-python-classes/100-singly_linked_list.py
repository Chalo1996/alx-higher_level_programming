#!/usr/bin/python3
"""Creates a class object"""

class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Class constructor for Node class"""
        self.__data = None
        self.__next_node = None
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for next_node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList class definition"""

    def __init__(self):
        """Class constructor for SinglyLinkedList class"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node in the correct sorted position in the list"""
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and \
                    current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """String representation of the linked list"""
        current = self.__head
        linked_list_str = ""
        while current:
            linked_list_str += str(current.data) + "\n"
            current = current.next_node
        linked_list_str = linked_list_str.rstrip("\n")
        return linked_list_str
