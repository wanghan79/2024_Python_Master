import time
import random
import string
from functools import wraps


class MethodStats:
    def __init__(self):
        self.call_count = 0
        self.total_time = 0.0

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()

            result = func(*args, **kwargs)

            end_time = time.time()
            elapsed_time = end_time - start_time

            self.call_count += 1
            self.total_time += elapsed_time

            return result

        # This allows access to the stats through the wrapper
        wrapper.call_count = lambda: self.call_count
        wrapper.total_time = lambda: self.total_time
        return wrapper


class RandomStructureGenerator:
    def __init__(self):
        pass

    def generate_random_value(self, value_type):
        if value_type == int:
            return random.randint(0, 100)
        elif value_type == float:
            return random.uniform(0, 100)
        elif value_type == str:
            return ''.join(random.sample(string.ascii_letters + string.digits, 8))
        elif value_type == bool:
            return random.choice([True, False])
        else:
            raise ValueError("Unsupported value type: {}".format(value_type))

    @MethodStats()
    def generate_random_structure(self, structure):
        if isinstance(structure, dict):
            return {k: self.generate_random_structure(v) for k, v in structure.items()}
        elif isinstance(structure, list):
            return [self.generate_random_structure(elem) for elem in structure]
        elif isinstance(structure, tuple):
            return tuple(self.generate_random_structure(elem) for elem in structure)
        elif isinstance(structure, set):
            return {self.generate_random_structure(elem) for elem in structure}
        elif isinstance(structure, type):
            return self.generate_random_value(structure)
        else:
            raise ValueError("Unsupported structure type: {}".format(type(structure)))


if __name__ == "__main__":
    generator = RandomStructureGenerator()
    input_structure = {
        'a': int,
        'b': [float, str],
        'c': {'d': bool, 'e': int},
        'f': (str, float)
    }

    # Generating random structures multiple times
    for _ in range(5):
        print(generator.generate_random_structure(input_structure))

    # Accessing the stats
    print(f"generate_random_structure was called {generator.generate_random_structure.call_count()} times.")
    print(f"Total execution time: {generator.generate_random_structure.total_time()} seconds.")
