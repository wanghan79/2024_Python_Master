import random
import string

class RandomStructureGenerator:
    def __init__(self, *args):
        self.args = args

    def random_value(self):
        return random.choice([
            random.randint(1, 100),  # 随机整数
            random.uniform(1.0, 100.0),  # 随机浮点数
            ''.join(random.choices(string.ascii_letters + string.digits, k=5)),  # 随机字符串
            None,  # None值
            True,  # 布尔值True
            False  # 布尔值False
        ])

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
    {"key1": [1, 2], "key2": (3, 4)},
    (5, 6),
    [7, 8]
]

generator = RandomStructureGenerator()
randomized_structure = generator.generate_random_structure(input_structure)
print(randomized_structure)
