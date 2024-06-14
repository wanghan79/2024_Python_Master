import random

class RandomStructureGenerator:
    def __init__(self):
        self.random = random.Random()

    def generate(self, structure):
        if isinstance(structure, list):
            return [self.generate(item) for item in structure]
        elif isinstance(structure, dict):
            return {key: self.generate(value) for key, value in structure.items()}
        elif isinstance(structure, int):
            return self.random.randint(0, structure)
        elif isinstance(structure, float):
            return self.random.uniform(0, structure)
        elif isinstance(structure, str):
            return ''.join(self.random.choice(structure) for _ in range(len(structure)))
        else:
            raise ValueError("Unsupported data type")
