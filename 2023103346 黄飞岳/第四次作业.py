import random
import string
from typing import Any, Generator

def generate_random_structure(structure: Any) -> Any:
    pass

def random_structure_generator(structure: Any) -> Generator:
    if isinstance(structure, dict):
        for k, v in structure.items():
            yield (k, generate_random_structure(v))
    elif isinstance(structure, list):
        for item in structure:
            yield generate_random_structure(item)
    elif isinstance(structure, tuple):
        for item in structure:
            yield generate_random_structure(item)
    elif isinstance(structure, (int, float, str)):
        yield generate_random_structure(structure)
    else:
        yield None

# 测试
if __name__ == "__main__":
    example_structure = {
        'a': [1, 2.0, 'three'],
        'b': {'c': 3, 'd': [4, 5.0]}
    }
    for item in random_structure_generator(example_structure):
        print(item)