#
# Author: Sareeb Hakak
# Purpose: Learn Linkedlist
# Date: 20 Feb 24
# In C++, use std::list

class Node:
    def __init__(self, data=None, next=None):
        """
        Creates a single Node to build a linked list
        :param data: Data stored in the node
        :type data: Any (int, float, char, object)
        :param next: Pointer to the next node
        :type next: Node
        """
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        """
        Create the general implementation of the linked list
        """
        self.head = None  # points to the head of the list

    def insert_at_beginning(self, data):
        """
        Insert a node at the start,
        attach pointer to the existing first element,
        and make the new node the head of the list

        :param data: data for first node that will be inserted
        :type data: Any
        :return: None
        """
        self.head = Node(data, self.head)

    def print(self):
        if self.head is None:
            print("LinkedList is empty")
            return

        current_node = self.head
        while current_node:  # this goes to the last
            print(current_node.data, end=" --> ")
            current_node = current_node.next  # this goes to None
        print("None")

    def append(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        current_node = self.head
        while current_node.next:  # this only get to second last
            current_node = current_node.next  # so that we get the last node

        current_node.next = Node(data, None)

    def insert_values(self, values):
        self.head = None
        for value in values:
            self.append(value)

    def get_length(self):
        current_node = self.head
        length = 0
        while current_node:
            length += 1
            current_node = current_node.next
        return length

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        current_node = self.head
        counter = 0
        while current_node:
            if counter == index - 1:
                current_node.next = current_node.next.next
                break
            current_node = current_node.next
            counter += 1

    def insert_at(self, index, value):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(value)

        current_node = self.head
        counter = 0
        while current_node:
            if counter == index - 1:
                node = Node(value)
                node.next = current_node.next
                current_node.next = node
                break
            current_node = current_node.next
            counter += 1

    def insert_after_value(self, data_after, value):
        current_node = self.head
        while current_node:
            if current_node.data == data_after:
                break
            current_node = current_node.next

        node = Node(value, current_node.next)
        current_node.next = node

    def remove_by_value(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next

        current_node = self.head
        while current_node:
            try:
                if current_node.next.data == value:
                    current_node.next = current_node.next.next
                else:
                    current_node = current_node.next
            except:
                return


if __name__ == '__main__':
    ll = LinkedList()
    data = [5, 4, 3, 2, 1]
    for i in data:
        ll.insert_at_beginning(i)
    ll.append(6)
    ll.append(7)
    ll.print()
    ll.remove_at(2)
    ll.print()
    print(ll.get_length())
    ll.insert_values([2, 4, 6, 8])
    ll.insert_at(2, 1)
    ll.print()
    ll.insert_after_value(8, 2)
    ll.insert_after_value(1, 2)
    ll.print()
    ll.remove_by_value(2)
    ll.print()
