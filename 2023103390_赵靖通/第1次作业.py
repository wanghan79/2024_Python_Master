"""
  -*- encoding: utf-8 -*-
  @Author: zhaojingtong
  @Time  : 2024/06/14 10:18
  @Email: 2665109868@qq.com
  @function
"""
# -*- encoding: utf-8 -*-
# @Author: zhaojingtong
# @Time  : 2024/06/14 10:18
# @Email: 2665109868@qq.com
# @function

import random

def generate_random_value(value, **kwargs):
    if isinstance(value, dict):
        return {key: generate_random_value(val, **kwargs) for key, val in value.items()}
    elif isinstance(value, list):
        return [generate_random_value(item, **kwargs) for item in value]
    elif isinstance(value, type):
        if value == int:
            return random.randint(kwargs.get('int_min', 0), kwargs.get('int_max', 10000))
        elif value == float:
            return random.uniform(kwargs.get('float_min', 0), kwargs.get('float_max', 1000))
        elif value == str:
            return ''.join(random.choices(kwargs.get('str_chars', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'), k=kwargs.get('str_len', 5)))
        else:
            return value
    else:
        return value

def recursive_traverse(data, **kwargs):
    for key, value in data.items():
        if isinstance(value, dict):
            data[key] = recursive_traverse(value, **kwargs)
        else:
            data[key] = generate_random_value(value, **kwargs)
    return data

# Define the desired data structure
data_structure = {
    'int_value': int,
    'str_value': str,
    'list_value': [int, str],
    'dict_value': {
        'nested_int': int
    }
}

if __name__ == '__main__':
    # You can pass additional arguments to control the random value generation
    random_data = recursive_traverse(data_structure, int_min=1, int_max=500, float_min=1.0, float_max=100.0, str_len=8)
    print(random_data)

