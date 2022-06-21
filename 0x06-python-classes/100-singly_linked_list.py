#!/usr/bin/python3
"""
This module defines a Singly linked list
"""


class Node:
    """Node implementation
    """
    def __init__(self, data, next_node=None):
        """Defines a node for a singly linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError('data must be an integer')

        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) != Node:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList implementation
    """
    def __init__(self):
        """Defines the singly linked list
        """
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        else:
            for sym in range(0, self.position[1]):
                print("")
            for sym in range(0, self.__size):
                for char in range(0, self.position[0]):
                    print(" ", end="")
                for char in range(0, self.__size - 1):
                    print("#", end="")
                print("#")
