import random
import string
from typing import Any, Dict, List, Tuple

class RandomStructureGenerator:
    def __init__(self, int_range: Tuple[int, int] = (0, 100), float_range: Tuple[float, float] = (0.0, 100.0), str_length: int = 10):
        self.int_range = int_range
        self.float_range = float_range
        self.str_length = str_length

    def generate(self, structure: Any) -> Any:
        if isinstance(structure, dict):
            return {k: self.generate(v) for k, v in structure.items()}
        elif isinstance(structure, list):
            return [self.generate(item) for item in structure]
        elif isinstance(structure, tuple):
            return tuple(self.generate(item) for item in structure)
        elif isinstance(structure, int):
            return random.randint(*self.int_range)
        elif isinstance(structure, float):
            return random.uniform(*self.float_range)
        elif isinstance(structure, str):
            return ''.join(random.choices(string.ascii_lowercase, k=self.str_length))
        else:
            return structure

# Example usage
example_structure = {
    'a': [1, 2.0, 'three'],
    'b': {'c': 3, 'd': [4, 5.0]}
}
generator = RandomStructureGenerator(int_range=(50, 150), float_range=(50.0, 150.0), str_length=15)
random_structure = generator.generate(example_structure)
print(random_structure)
