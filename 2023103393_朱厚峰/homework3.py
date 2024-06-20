#统计方法修饰器实现
import random
from functools import wraps


class RandomDataGenerator:
    def __init__(self):
        pass

    def validate_structure(func):
        def wrapper(self, structure, *args, **kwargs):

            valid_types = (int, float, str, dict, list, tuple, set)
            if not isinstance(structure, valid_types):
                raise ValueError("Invalid data structure. Must be one of: int, float, str, dict, list, tuple, set.")
            return func(self, structure, *args, **kwargs)

        return wrapper

    def generate_random_data(self, structure, *args, **kwargs):
        def generate_random_item(item, *args, **kwargs):
            if isinstance(item, int):
                return random.randint(*args)
            elif isinstance(item, float):
                return random.uniform(*args)
            elif isinstance(item, str):
                return ''.join(random.choices(kwargs['charset'], k=len(item)))
            elif isinstance(item, dict):
                return {key: generate_random_item(value, *args, **kwargs) for key, value in item.items()}
            elif isinstance(item, list):
                return [generate_random_item(element, *args, **kwargs) for element in item]
            elif isinstance(item, tuple):
                return tuple(generate_random_item(element, *args, **kwargs) for element in item)
            elif isinstance(item, set):
                return {generate_random_item(element, *args, **kwargs) for element in item}
            else:
                raise ValueError(f"Unsupported data type: {type(item)}")

        return generate_random_item(structure, *args, **kwargs)


structure = {'a': [10, 5.0, 'abc', True], 'b': (1, 2, 3), 'c': {'x', 'y', 'z'}}
generator = RandomDataGenerator()
random_data = generator.generate_random_data(structure, 1, 100, charset='abcdefghijklmnopqrstuvwxyz')
print(random_data)
