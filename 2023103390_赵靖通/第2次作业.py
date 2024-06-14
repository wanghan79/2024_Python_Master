# -*- encoding: utf-8 -*-
# @Author: zhaojingtong
# @Time  : 2024/06/14 10:18
# @Email: 2665109868@qq.com
# @function

import random

class RandomStructureGenerator:
    def __init__(self, int_min=0, int_max=10000, float_min=0.0, float_max=1000.0, str_len=5, str_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        self.int_min = int_min
        self.int_max = int_max
        self.float_min = float_min
        self.float_max = float_max
        self.str_len = str_len
        self.str_chars = str_chars

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
