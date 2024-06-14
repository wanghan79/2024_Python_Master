import random
import string

class RandomStructureGenerator:
    def __init__(self):
        pass

    def random_value(self):
        options = [
            random.randint(1, 100),
            random.uniform(1.0, 100.0),
            ''.join(random.choices(string.ascii_letters + string.digits, k=5)),
            None,
            True,
            False
        ]
        return random.choice(options)

    def generate_random_structure(self, structure):
        if isinstance(structure, list):
            return [self.generate_random_structure(item) for item in structure]
        elif isinstance(structure, tuple):
            return tuple(self.generate_random_structure(item) for item in structure)
        elif isinstance(structure, dict):
            return {key: self.generate_random_structure(value) for key, value in structure.items()}
        else:
            return self.random_value()

input_structure = [
    {"key1": [2, 3], "key2": (4, 5)},
    (6, 7),
    [8, 9]
]

generator = RandomStructureGenerator()
randomized_structure = generator.generate_random_structure(input_structure)
print(randomized_structure)