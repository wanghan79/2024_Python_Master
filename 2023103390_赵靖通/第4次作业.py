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

    def generate_random_data(self, data_structure, num_entries=1):
        def _recursive_traverse(data):
            if isinstance(data, dict):
                for key, value in data.items():
                    if isinstance(value, dict):
                        yield (key, dict(_recursive_traverse(value)))
                    else:
                        yield (key, self.generate_random_value(value))
            else:
                yield self.generate_random_value(data)

        return [dict(_recursive_traverse(data_structure)) for _ in range(num_entries)]

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
    num_entries = 5  # Specify the number of entries you want to generate
    random_data = generator.generate_random_data(data_structure, num_entries)
    for entry in random_data:
        print(entry)
