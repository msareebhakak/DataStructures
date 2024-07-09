
class TreeNode:
    def __init__(self, designation, name):
        self.name = name
        self.designation = designation
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

    def print_tree(self, key, level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        p = self.parent
        prefix = spaces + "|__" if p else ""

        if key == "name":
            print(prefix + self.name)
        elif key == "designation":
            print(prefix + self.designation)
        elif key == "both":
            print(prefix + f"{self.name} ({self.designation})")
        if self.children:
            for child in self.children:
                child.print_tree(key, level)


def build_tree():
    root = TreeNode("CEO", "A")

    level_1_0 = TreeNode("CTO", "B")
    level_1_0.add_child(TreeNode("Infrasture Head", "F"))
    level_1_0.add_child(TreeNode("Application Head", "G"))

    level_1_1 = TreeNode("HR Head", "C")
    level_1_1.add_child(TreeNode("Recruitment Head", "D"))
    level_1_1.add_child(TreeNode("Policy Manager", "E"))

    root.add_child(level_1_0)
    root.add_child(level_1_1)

    return root


if __name__ == '__main__':
    tree = build_tree()
    tree.print_tree("name", 2)
    tree.print_tree("designation", 2)
    tree.print_tree("both", 2)

