class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        spaces = self.get_level() * " "
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children: #HA VAN GYEREKE, akkor hívjuk meg rekurzívan!!
            for child in self.children:
                child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

def build_product_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode("Laptop")
    root.add_child(laptop)
    return root

if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()
    