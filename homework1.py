import random
import string
from typing import Any, Dict, List, Tuple


def generate_random_structure(structure: Any, int_range: Tuple[int, int] = (0, 100),
                              float_range: Tuple[float, float] = (0.0, 100.0), str_length: int = 10) -> Any:

    if isinstance(structure, dict):
        return {k: generate_random_structure(v, int_range, float_range, str_length) for k, v in structure.items()}
    elif isinstance(structure, list):
        return [generate_random_structure(item, int_range, float_range, str_length) for item in structure]
    elif isinstance(structure, tuple):
        return tuple(generate_random_structure(item, int_range, float_range, str_length) for item in structure)
    elif isinstance(structure, int):
        return random.randint(*int_range)
    elif isinstance(structure, float):
        return random.uniform(*float_range)
    elif isinstance(structure, str):
        return ''.join(random.choices(string.ascii_lowercase, k=str_length))
    else:
        return structure


# Example usage
example_structure = {
    'a': [1, 2.0, 'three'],
    'b': {'c': 3, 'd': [4, 5.0]}
}
random_structure = generate_random_structure(example_structure)
print(random_structure)
