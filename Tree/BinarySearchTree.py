#
# Author: Sareeb Hakak
# Purpose: Learn Binary Search Tree DS
# Date: 28 Feb 24
#
# Each Node has at most 2 child nodes
# All values left to any node are less, and elements are always unique
# DFS: preorder, inorder, postorder
# BFS: level order

from collections import deque


class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)

        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def search(self, data):
        if self.data == data:
            return True

        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False

        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def get_sum(self):
        return sum(self.in_order_traversal())

    def in_order_traversal(self):
        # visit left side of tree, then base, then the right side of tree
        # L D R (left, data, right)
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        # visit the base, then left side of tree, then the right side of tree
        # D L R (data, left, right)
        elements = [self.data]

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        # visit left side of tree, then the right side of tree, then the base
        # L R D (left, right, data)
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def level_order_traversal(self):
        # BFS search, we use a Queue
        # Add a node to Queue, then before popping out append it children
        result = []
        tree_queue = deque()
        tree_queue.append(self)  # start with the root

        while tree_queue:
            node = tree_queue.popleft()
            result.append(node.data)

            # visit its children
            if node.left:
                tree_queue.append(node.left)
            if node.right:
                tree_queue.append(node.right)
        return result

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        elif val == self.data:
            # no child
            if self.left is None and self.right is None:
                print("Deleting leaf node:", self.data)
                return None
            # one child
            if self.left is None:
                print("Deleting node with one child (right):", self.data)
                return self.right
            elif self.right is None:
                print("Deleting node with one child (left):", self.data)
                return self.left
            # two child
            else:
                print("Deleting node with two children:", self.data)
                min_val = self.right.find_min()
                self.data = min_val
                self.right = self.right.delete(min_val)
                # max_val = self.left.find_max()
                # self.data = max_val
                # self.left = self.left.delete(max_val)

        return self


def build_tree(values):
    root = BinarySearchTree(values[0])
    for i in range(1, len(values)):
        root.add_child(values[i])

    return root


if __name__ == '__main__':
    bst = build_tree([7, 4, 1, 20, 9, 23, 18, 34])
    print(bst.in_order_traversal())
    print(bst.pre_order_traversal())
    print(bst.post_order_traversal())
    print(bst.level_order_traversal())
    # print(bst.search(20))
    # print(bst.find_min())
    # print(bst.find_max())
    # print(bst.get_sum())
    # bst.delete(20)
    # print(bst.in_order_traversal())
    # bst2 = build_tree([7, 2])
    # print(bst2.in_order_traversal())
    # bst2.delete(2)
    # print(bst2.in_order_traversal())
