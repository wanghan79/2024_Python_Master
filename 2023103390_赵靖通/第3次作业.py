# -*- encoding: utf-8 -*-
# @Author: zhaojingtong
# @Time  : 2024/06/14 10:18
# @Email: 2665109868@qq.com
# @function

import random
from functools import wraps

class RandomStructureGenerator:
    def __init__(self, int_min=0, int_max=10000, float_min=0.0, float_max=1000.0, str_len=5, str_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        self.int_min = int_min
        self.int_max = int_max
        self.float_min = float_min
        self.float_max = float_max
        self.str_len = str_len
        self.str_chars = str_chars
        self.stats = {
            'int_count': 0,
            'float_count': 0,
            'str_count': 0,
            'list_count': 0,
            'dict_count': 0
        }

    def track_stats(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            value = args[0]
            if isinstance(value, int):
                self.stats['int_count'] += 1
            elif isinstance(value, float):
                self.stats['float_count'] += 1
            elif isinstance(value, str):
                self.stats['str_count'] += 1
            elif isinstance(value, list):
                self.stats['list_count'] += 1
            elif isinstance(value, dict):
                self.stats['dict_count'] += 1
            return func(self, *args, **kwargs)
        return wrapper

    @track_stats
    def generate_random_value(self, value):
        if isinstance(value, dict):
            return {key: self.generate_random_value(val) for key, val in value.items()}
        elif isinstance(value, list):
            return [self.generate_random_value(item) for item in value]
        elif isinstance(value, type):
            if value == int:
                return random.randint(self.int_min, self.int_max)
            elif value == float:
                return random.uniform(self.float_min, self.float_max)
            elif value == str:
                return ''.join(random.choices(self.str_chars, k=self.str_len))
            else:
                return value
        else:
            return value

    def recursive_traverse(self, data):
        for key, value in data.items():
            if isinstance(value, dict):
                data[key] = self.recursive_traverse(value)
            else:
                data[key] = self.generate_random_value(value)
        return data

    def get_stats(self):
        return self.stats

if __name__ == '__main__':
    # Define the desired data structure
    data_structure = {
        'int_value': int,
        'str_value': str,
        'list_value': [int, str],
        'dict_value': {
            'nested_int': int
        }
    }

    # Create an instance of the class
    generator = RandomStructureGenerator(int_min=1, int_max=500, float_min=1.0, float_max=100.0, str_len=8)

    # Generate the random data
    random_data = generator.recursive_traverse(data_structure)
    print(random_data)

    # Print the statistics
    stats = generator.get_stats()
    print(stats)
