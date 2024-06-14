import random
import string
from typing import Any, Dict, List, Union

def generate_random_structure(structure: Any) -> Any:
    if isinstance(structure, dict):
        return {k: generate_random_structure(v) for k, v in structure.items()}
    elif isinstance(structure, list):
        return [generate_random_structure(item) for item in structure]
    elif isinstance(structure, tuple):
        return tuple(generate_random_structure(item) for item in structure)
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
random_structure = generate_random_structure(example_structure)
print(random_structure)

