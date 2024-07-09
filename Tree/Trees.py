#
# Author: Sareeb Hakak
# Purpose: Learn Tree DS
# Date: 26 Feb 24
#

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        counter = 0
        p = self.parent
        while p:
            counter += 1
            p = p.parent
        return counter

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        p = self.parent
        prefix = spaces + "|__" if p else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Samsung"))
    cellphone.add_child(TreeNode("Pixel"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


if __name__ == '__main__':
    d = {
        'Electronics': {
            'Laptop': ['Macbook', 'Surface', 'Thinkpad'],
            'Cellphone': ['Iphone', 'Samsung', 'Pixel'],
            'Television': ['Samsung', 'LG']
        }
    }

    print(d)

    tree = build_tree()
    tree.print_tree()
    # print(tree.get_level())
    # print(tree.children[0].children[0].get_level())
