#
# Author: Sareeb Hakak
# Purpose: Learn DoubleLinkedlist
# Date: 21 Feb 24
#

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Empty Linkedlist")
            return

        current_node = self.head
        while current_node:
            print(current_node.data, end=" <--> ")
            current_node = current_node.next
        print("None")

    def print_reverse(self):
        if self.head is None:
            print("Empty Linkedlist")
            return

        current_node = self.head
        while current_node.next:  # stop at second last one
            current_node = current_node.next  # this becomes the last one
        while current_node:
            print(current_node.data, end=" <--> ")
            current_node = current_node.prev
        print("None")

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        node = Node(data, self.head, None)
        self.head.prev = node
        self.head = node

    def append(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next  # we stop at last
        node = Node(data, None, current_node)
        current_node.next = node

    def insert_values(self, values):
        for value in values:
            self.append(value)

    def get_length(self):
        current_node = self.head
        counter = 0
        while current_node:
            counter += 1
            current_node = current_node.next
        return counter

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise AttributeError("index out of range")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None

        current_node = self.head
        counter = 0
        while current_node:
            if counter == index - 1:
                current_node.next = current_node.next.next
                current_node.next.prev = current_node
            else:
                current_node = current_node.next
            counter += 1

    def insert_at(self, index, value):
        if index < 0 or index > self.get_length():
            raise AttributeError("index out of range")

        if index == 0:
            self.insert_at_beginning(value)

        counter = 0
        current_node = self.head
        node = Node(value, None, None)
        while current_node:
            if counter == index - 1:
                node.next = current_node.next
                node.prev = current_node
                current_node.next.prev = node
                current_node.next = node
            else:
                current_node = current_node.next
            counter += 1

    def insert_after_value(self, data_after, value):
        counter = 0
        current_node = self.head
        while current_node:
            if current_node.data == data_after:
                break
            current_node = current_node.next
            counter += 1
        node = Node(value, current_node.next, current_node)
        current_node.next = node

    def remove_by_value(self, value):
        if self.head is None:
            return
        if self.head.data == value:
            self.head = None

        counter = 0
        current_node = self.head
        while current_node:
            if current_node.next.data == value:
                break
            current_node = current_node.next
            counter += 1

        current_node.next = current_node.next.next
        current_node.next.prev = current_node


if __name__ == '__main__':
    ll = DoubleLinkedList()
    data = [5, 4, 3, 2, 1]
    for i in data:
        ll.insert_at_beginning(i)
    ll.append(6)
    ll.insert_values([7, 8, 9])
    ll.print_forward()
    ll.print_reverse()
    print(ll.get_length())
    ll.remove_at(5)
    ll.insert_at(5, 100)
    ll.insert_after_value(9, 10)
    ll.remove_by_value(5)
    ll.print_forward()
    ll.print_reverse()
