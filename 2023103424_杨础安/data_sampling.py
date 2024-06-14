import random
from functools import wraps


class RandomDataGenerator:
    def __init__(self):
        pass

    def validate_structure(func):
        @wraps(func)
        def wrapper(self, structure, *args, **kwargs):
            # Check if the structure is a valid data structure
            valid_types = (int, float, str, dict, list, tuple, set)
            if not isinstance(structure, valid_types):
                raise ValueError("Invalid data structure. Must be one of: int, float, str, dict, list, tuple, set.")
            return func(self, structure, *args, **kwargs)

        return wrapper

    @validate_structure
    def generate_random_data(self, structure, *args, **kwargs):
        """
        Generate random data based on the given structure.

        Args:
            structure: A valid data structure.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            A list containing random data based on the given structure.
        """

        def generate_random_item(item, *args, **kwargs):
            # Check the data type of the item and generate random data accordingly
            if isinstance(item, int):
                return random.randint(args[0], args[1])  # 修改此处调用方式
            elif isinstance(item, float):
                return random.uniform(args[0], args[1])  # 修改此处调用方式
            elif isinstance(item, str):
                return ''.join(random.choices(kwargs['charset'], k=len(item)))  # 修改此处调用方式
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


# Example usage:
structure = {'a': [10, 5.0, 'abc', True], 'b': (1, 2, 3), 'c': {'x', 'y', 'z'}}
generator = RandomDataGenerator()
random_data = generator.generate_random_data(structure, 1, 100, charset=['abcdefghijklmnopqrstuvwxyz'])
print(random_data)
