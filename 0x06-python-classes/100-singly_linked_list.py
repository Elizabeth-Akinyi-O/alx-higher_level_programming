#!/usr/bin/python3

"""Define a singly list  class."""


class Node:
    """Represent a node in a singly linked list - body."""

    def __init__(self, data, next_node=None):
        """Initialize - new Node.

        Args:
            data (int): data of the new node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/Set the data of the node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter and setter for data of the node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a SinglyLinkedList."""

    def __init__(self):
        """Initialize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node to the SinglyLinkedList.

        Inserts a new Node into the correct sorted position
        in the list (increasing order).

        Args:
            value (Node): New node to be inserted.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """Define the string method (print ()) for a SinglyLinkedList."""
        nodes = []
        temp = self.__head
        while temp is not None:
            nodes.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(nodes))
