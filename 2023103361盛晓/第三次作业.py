import random
import string
from typing import Any, Dict, List, Union

class RandomStructureGenerator:
    def __init__(self):
        pass

    def generate(self, structure: Any) -> Any:
        if isinstance(structure, dict):
            return {k: self.generate(v) for k, v in structure.items()}
        elif isinstance(structure, list):
            return [self.generate(item) for item in structure]
        elif isinstance(structure, tuple):
            return tuple(self.generate(item) for item in structure)
        elif isinstance(structure, int):
            return random.randint(0, 100)
        elif isinstance(structure, float):
            return random.uniform(0.0, 100.0)
        elif isinstance(structure, str):
            return ''.join(random.choices(string.ascii_lowercase, k=10))
        else:
            return structure

# Example usage
example_structure = {
    'a': [1, 2.0, 'three'],
    'b': {'c': 3, 'd': [4, 5.0]}
}
generator = RandomStructureGenerator()
random_structure = generator.generate(example_structure)
print(random_structure)

