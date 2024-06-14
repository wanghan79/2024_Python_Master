import random
import string
from typing import Any

class RandomStructureGenerator:
    def __init__(self):
        pass

    def generate(self, structure: Any) -> Any:
        if isinstance(structure, dict):
            return {k: self.generate(v) for k, v in structure.items()}
        elif isinstance(structure, list):
            return [self.generate(v) for v in structure]
        elif isinstance(structure, tuple):
            return tuple(self.generate(v) for v in structure)
        elif isinstance(structure, int):
            return random.randint(1, 100)
        elif isinstance(structure, float):
            return round(random.uniform(1.0, 100.0), 2)
        elif isinstance(structure, str):
            length = random.randint(5, 15)
            return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        else:
            return structure

# 测试
if __name__ == "__main__":
    generator = RandomStructureGenerator()
    example_structure = {
        'a': [1, 2.0, 'three'],
        'b': {'c': 3, 'd': [4, 5.0]}
    }
    print("随机结构:", generator.generate(example_structure))