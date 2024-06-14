import random
import string

class TreeNode:
    def __init__(self, key=None, type=None):
        self.key = key
        self.type = type
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class TreeBuilder:
    def __init__(self, struct):
        self.root = self.build_tree(struct)

    def build_tree(self, struct):
        if isinstance(struct, dict):
            node = TreeNode(type='dict')
            for key, value in struct.items():
                child = self.build_tree(value)
                child.key = key
                node.add_child(child)
            return node
        elif isinstance(struct, list):
            node = TreeNode(type='list')
            for item in struct:
                child = self.build_tree(item)
                node.add_child(child)
            return node
        else:
            return TreeNode(type=struct)

    def generate_value(self, type):
        if type == 'int':
            return random.randint(0, 100)
        elif type == 'float':
            return random.uniform(0, 100)
        elif type == 'str':
            length = random.randint(5, 10)
            return ''.join(random.choices(string.ascii_letters, k=length))
        else:
            return None

    def print_tree(self, node, is_last=True, level=0):
        if node.type == 'dict':
            print("{", end="")
            for i, child in enumerate(node.children):
                print(f"{child.key!r}: ", end="")
                self.print_tree(child, i == len(node.children) - 1, level + 1)
                if not is_last and i < len(node.children) - 1:
                    print(", ", end="")
            print("}", end="")
        elif node.type == 'list':
            print("[", end="")
            for i, child in enumerate(node.children):
                self.print_tree(child, i == len(node.children) - 1, level + 1)
                if not is_last and i < len(node.children) - 1:
                    print(", ", end="")
            print("]", end="")
        else:
            value = self.generate_value(node.type)
            print(f"{value!r}", end="")
            if not is_last:
                print(", ", end="")

    def display(self):
        self.print_tree(self.root)

def display_tree2(input_struct):
    tree_builder = TreeBuilder(input_struct)
    tree_builder.display()
