import random
import string

class RandomStructureGenerator:
    def __init__(self):
        pass

    def generate_random_int(self):
        return random.randint(1, 100)

    def generate_random_float(self):
        return random.uniform(1.0, 100.0)

    def generate_random_string(self, length=5):
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def generate_random_structure(self, structure):
        if isinstance(structure, int):
            return self.generate_random_int()
        elif isinstance(structure, float):
            return self.generate_random_float()
        elif isinstance(structure, str):
            return self.generate_random_string(len(structure))
        elif isinstance(structure, list):
            return [self.generate_random_structure(item) for item in structure]
        elif isinstance(structure, dict):
            return {key: self.generate_random_structure(value) for key, value in structure.items()}
        else:
            return None

# 示例
generator = RandomStructureGenerator()
input_structure = [23.3423543, [2, "abc"], {"key1": 3, "key2": "def"}]
print(generator.generate_random_structure(input_structure))
