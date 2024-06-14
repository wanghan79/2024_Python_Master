import random

class RandomStructureGenerator:
    def generate(self, structure):
        if isinstance(structure, int):
            return random.randint(0, 100)
        elif isinstance(structure, float):
            return random.uniform(0, 1)
        elif isinstance(structure, bool):
            return random.choice([True, False])
        elif isinstance(structure, list):
            return [self.generate(item) for item in structure]
        elif isinstance(structure, tuple):
            return tuple(self.generate(item) for item in structure)
        elif isinstance(structure, dict):
            return {key: self.generate(value) for key, value in structure.items()}
        else:
            raise ValueError("Unsupported data type")

# 测试代码
structure = {"a": 1, "b": [2, 3.0], "c": (True, False), "d": {"e": 5, "f": 6.0}}
generator = RandomStructureGenerator()
random_structure = generator.generate(structure)
print(random_structure)
