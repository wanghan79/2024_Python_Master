import random
import json
from ast import literal_eval
from statistics import mean

class TreeNode:
    def __init__(self, data_type, value):
        self.data_type = data_type
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def parse_data(self, data, parent=None):
        if isinstance(data, dict):
            node = TreeNode("dict", None)
            for key, value in data.items():
                child_node = self.parse_data(value)
                child_node.value = key
                node.add_child(child_node)
        elif isinstance(data, list) or isinstance(data, tuple):
            node = TreeNode("list", None)
            for item in data:
                child_node = self.parse_data(item)
                node.add_child(child_node)
        else:
            node = TreeNode(type(data).__name__, data)
        return node

    def generate_random_data(self, n):
        data_generators = {
            "int": lambda: random.randint(0, 100),
            "float": lambda: round(random.uniform(0, 100), 2),
            "bool": lambda: random.choice([True, False]),
            "str": lambda: ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=5))
        }
        if self.data_type == "dict":
            return [self._generate_random_dict() for _ in range(n)]
        elif self.data_type == "list":
            return [self._generate_random_list() for _ in range(n)]
        elif self.data_type == "tuple":
            return [tuple(self._generate_random_list()) for _ in range(n)]
        else:
            return [data_generators[self.data_type]() for _ in range(n)]

    def _generate_random_dict(self):
        return {child.value: child.generate_random_data(1)[0] for child in self.children}

    def _generate_random_list(self):
        return [child.generate_random_data(1)[0] for child in self.children]

    def calculate_stats(self, data_list):
        stats = {
            'int': {'total': 0, 'count': 0, 'average': 0},
            'float': {'total': 0, 'count': 0, 'average': 0}
        }
        for data in data_list:
            self._calculate_recursive(data, stats)
        for data_type in stats:
            if stats[data_type]['count'] > 0:
                stats[data_type]['average'] = stats[data_type]['total'] / stats[data_type]['count']
        return stats

    def _calculate_recursive(self, data, stats):
        if isinstance(data, dict):
            for value in data.values():
                self._calculate_recursive(value, stats)
        elif isinstance(data, list):
            for item in data:
                self._calculate_recursive(item, stats)
        elif isinstance(data, int) or isinstance(data, float):
            stats_type = 'int' if isinstance(data, int) else 'float'
            stats[stats_type]['total'] += data
            stats[stats_type]['count'] += 1

# 装饰器示例，用于打印方法执行时间
from functools import wraps
import time

def stats_decorator(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        start_time = time.time()
        result = func(self, *args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"{func.__name__} executed in {elapsed_time:.4f} seconds")
        return result
    return wrapper

# 应用装饰器
TreeNode.calculate_stats = stats_decorator(TreeNode.calculate_stats)