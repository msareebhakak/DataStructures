class Component:
    """Abstract class representing both primitive leaf objects and composite objects"""

    def operation(self):
        pass


class Leaf(Component):
    """Concrete class representing leaf objects in the composition"""

    def operation(self):
        return "Leaf"


class Composite(Component):
    """Concrete class representing complex components that have children"""

    def __init__(self):
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def operation(self):
        results = []
        for child in self._children:
            results.append(child.operation())
        return "Branch(" + '+'.join(results) + ")"


if __name__ == '__main__':
    # Usage
    leaf = Leaf()
    composite = Composite()
    composite.add(leaf)

    tree = Composite()
    tree.add(composite)

    print(tree.operation())
