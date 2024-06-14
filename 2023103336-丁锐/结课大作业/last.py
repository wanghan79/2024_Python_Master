import random
import string

class RandomStructureGenerator:
    def __init__(self):
        pass

    def random_value(self):
        return random.choice([
            random.randint(1, 100),
            random.uniform(1.0, 100.0),
            ''.join(random.choices(string.ascii_letters + string.digits, k=5)),
            None,
            True,
            False
        ])

    def random_structure(self, structure):
        if isinstance(structure, list):
            return [self.random_structure(item) for item in structure]
        elif isinstance(structure, tuple):
            return tuple(self.random_structure(item) for item in structure)
        elif isinstance(structure, dict):
            return {key: self.random_structure(value) for key, value in structure.items()}
        else:
            return self.random_value()

def random_structure_generator(structure):
    generator = RandomStructureGenerator()
    while True:
        yield generator.random_structure(structure)

# 示例
input_structure = [
    {"key1": [1, 2], "key2": (3, 4)},
    (5, 6),
    [7, 8]
]

gen = random_structure_generator(input_structure)
print(next(gen))
print(next(gen))
