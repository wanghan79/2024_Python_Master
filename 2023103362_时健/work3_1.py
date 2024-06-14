import random
import string

class TreeNode:
    def __init__(self, key=None, type=None):
        self.key = key
        self.type = type
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def build_tree(struct):
    if isinstance(struct, dict):
        node = TreeNode(type='dict')
        for key, value in struct.items():
            child = build_tree(value)
            child.key = key
            node.add_child(child)
        return node
    elif isinstance(struct, list):
        node = TreeNode(type='list')
        for item in struct:
            child = build_tree(item)
            node.add_child(child)
        return node
    else:
        return TreeNode(type=struct)

def generate_value(type):
    if type == 'int':
        return random.randint(0, 100)
    elif type == 'float':
        return random.uniform(0, 100)
    elif type == 'str':
        length = random.randint(5, 10)
        return ''.join(random.choices(string.ascii_letters, k=length))
    else:
        return None

def print_tree(node, is_last=True, level=0):
    if node.type == 'dict':
        print("{", end="")
        for i, child in enumerate(node.children):
            print(f"{child.key!r}: ", end="")
            print_tree(child, i == len(node.children) - 1, level + 1)
            if not is_last and i < len(node.children) - 1:
                print(", ", end="")
        print("}", end="")
    elif node.type == 'list':
        print("[", end="")
        for i, child in enumerate(node.children):
            print_tree(child, i == len(node.children) - 1, level + 1)
            if not is_last and i < len(node.children) - 1:
                print(", ", end="")
        print("]", end="")
    else:
        value = generate_value(node.type)
        print(f"{value!r}", end="")
        if not is_last:
            print(", ", end="")
# 定义装饰器
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

# 使用装饰器
@count_calls
def display_tree3_1(struct):
    root = build_tree(struct)
    print_tree(root)
    print(f"\ndisplay_tree1 was called {display_tree3_1.calls} times.")
