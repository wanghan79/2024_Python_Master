import random
import string

def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        result = func(*args, **kwargs)
        print(f"{func.__name__} called {wrapper.calls} times")
        return result
    wrapper.calls = 0
    return wrapper

class RandomStructureGeneratorWithStats:
    def __init__(self):
        pass

    @count_calls
    def random_value(self):
        return random.choice([
            random.randint(1, 100),
            random.uniform(1.0, 100.0),
            ''.join(random.choices(string.ascii_letters + string.digits, k=5)),
            None,
            True,
            False
        ])

    @count_calls
    def random_structure(self, structure):
        if isinstance(structure, list):
            return [self.random_structure(item) for item in structure]
        elif isinstance(structure, tuple):
            return tuple(self.random_structure(item) for item in structure)
        elif isinstance(structure, dict):
            return {key: self.random_structure(value) for key, value in structure.items()}
        else:
            return self.random_value()

# 示例
generator_with_stats = RandomStructureGeneratorWithStats()
randomized_structure_with_stats = generator_with_stats.random_structure(input_structure)
print(randomized_structure_with_stats)
