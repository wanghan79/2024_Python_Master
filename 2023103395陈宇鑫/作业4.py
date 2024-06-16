import random
import string
import networkx as nx



# 树节点类
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)



class RandomStructureGenerator:
    def __init__(self):
        pass

    def generate_random_int(self, min_value, max_value):
        """
        生成一个随机整数。
        :param min_value: 整数的最小值。
        :param max_value: 整数的最大值。
        :return: 一个在指定范围内的随机整数。
        """
        return random.randint(min_value, max_value)

    def generate_random_float(self, min_value, max_value):
        """
        生成一个随机浮点数。
        :param min_value: 浮点数的最小值。
        :param max_value: 浮点数的最大值。
        :return: 一个在指定范围内的随机浮点数。
        """
        return random.uniform(min_value, max_value)

    def generate_random_char(self):
        """
        生成一个随机字符。
        :return: 一个随机字符。
        """
        return random.choice(string.ascii_letters)

    def generate_random_string(self, min_length, max_length):
        """
        生成一个随机字符串。
        :param min_length: 字符串的最小长度。
        :param max_length: 字符串的最大长度。
        :return: 一个在指定长度范围内的随机字符串。
        """
        length = random.randint(min_length, max_length)
        return ''.join(random.choices(string.ascii_letters, k=length))

    def generate_random_bool(self):
        """
        生成一个随机布尔值。
        :return: 一个随机布尔值。
        """
        return random.choice([True, False])

    def generate_random_tuple(self, tuple_length, min_value, max_value):
        """
        生成一个随机元组。
        :param tuple_length: 元组的长度。
        :param min_value: 元素的最小值。
        :param max_value: 元素的最大值。
        :return: 一个在指定长度和值范围内的随机元组。
        """
        return tuple(random.randint(min_value, max_value) for _ in range(tuple_length))

    def generate_random_tree(self, max_depth, max_children):
        """
        递归地生成一个随机树。
        :param max_depth: 树的最大深度。
        :param max_children: 每个节点的最大子节点数。
        :return: 树的根节点。
        """
        if max_depth <= 0 or random.random() > 0.5:
            return None

        root = TreeNode(random.randint(0, 100))
        num_children = random.randint(1, max_children)
        for _ in range(num_children):
            child = self.generate_random_tree(max_depth - 1, max_children)
            if child:
                root.add_child(child)

        return root

    def generate_random_graph(self, num_nodes, num_edges):
        """
        生成一个随机图。
        :param num_nodes: 图的节点数。
        :param num_edges: 图的边数。
        :return: 一个随机图。
        """
        G = nx.Graph()
        for i in range(num_nodes):
            G.add_node(i, value=random.randint(0, 100))
        for _ in range(num_edges):
            node1, node2 = random.sample(range(num_nodes), 2)
            G.add_edge(node1, node2)
        return G

    def generate_random_set(self, max_size):
        """
        生成一个随机集合。
        :param max_size: 集合的最大大小。
        :return: 一个随机集合。
        """
        return set(random.sample(range(100), random.randint(1, max_size)))

    def generate_random_dict(self, max_size):
        """
        生成一个随机字典。
        :param max_size: 字典的最大大小。
        :return: 一个随机字典。
        """
        return {f"key_{i}": random.randint(0, 100) for i in range(random.randint(1, max_size))}

    def print_tree(self, node, level=0):
        """
        打印树的结构。
        :param node: 当前节点。
        :param level: 当前层级。
        """
        if node is None:
            return
        print("  " * level + str(node.value))
        for child in node.children:
            self.print_tree(child, level + 1)

    def print_graph(self, G):
        """
        打印图的结构。
        :param G: 一个图。
        """
        print("Graph nodes:")
        for node, attr in G.nodes(data=True):
            print(f"Node {node}: {attr['value']}")
        print("Graph edges:")
        for edge in G.edges():
            print(f"Edge between {edge[0]} and {edge[1]}")

    def print_set(self, s):
        """
        打印集合。
        :param s: 一个集合。
        """
        print(f"Set: {s}")

    def print_dict(self, d):
        """
        打印字典。
        :param d: 一个字典。
        """
        print("Dictionary:")
        for key, value in d.items():
            print(f"{key}: {value}")

# 树节点类
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)







# 实例化生成器
generator = RandomStructureGenerator()

# 生成并打印一个随机整数
print("Random Integer:", generator.generate_random_int(1, 100))

# 生成并打印一个随机浮点数
print("Random Float:", generator.generate_random_float(1.0, 100.0))

# 生成并打印一个随机字符
print("Random Character:", generator.generate_random_char())

# 生成并打印一个随机字符串
print("Random String:", generator.generate_random_string(5, 10))

# 生成并打印一个随机布尔值
print("Random Boolean:", generator.generate_random_bool())

# 生成并打印一个随机元组
print("Random Tuple:", generator.generate_random_tuple(5, 1, 100))


# 生成并打印一个随机树
print("Random Tree:")
tree = generator.generate_random_tree(4, 3)
generator.print_tree(tree)

# 生成并打印一个随机图
print("\nRandom Graph:")
graph = generator.generate_random_graph(5, 7)
generator.print_graph(graph)

# 生成并打印一个随机集合
print("\nRandom Set:")
s = generator.generate_random_set(10)
generator.print_set(s)

# 生成并打印一个随机字典
print("\nRandom Dictionary:")
d = generator.generate_random_dict(10)
generator.print_dict(d)