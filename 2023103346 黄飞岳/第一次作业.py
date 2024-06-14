import random
import string
from typing import Any, Dict, List, Union, Tuple

def generate_random_structure(structure: Any) -> Any:
    if isinstance(structure, dict):
        return {k: generate_random_structure(v) for k, v in structure.items()}
    elif isinstance(structure, list):
        return [generate_random_structure(v) for v in structure]
    elif isinstance(structure, tuple):
        return tuple(generate_random_structure(v) for v in structure)
    elif isinstance(structure, int):
        return random.randint(1, 100)
    elif isinstance(structure, float):
        return round(random.uniform(1.0, 100.0), 2)
    elif isinstance(structure, str):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 15)))
    else:
        return structure

# 测试
if __name__ == "__main__":
    example_structure = {
        'a': [1, 2.0, 'three'],
        'b': {'c': 3, 'd': [4, 5.0]}
    }
    print("原始结构:", example_structure)
    print("随机结构:", generate_random_structure(example_structure))