import random

def generate_random_structure(structure):
    if isinstance(structure, int):
        return random.randint(0, 100)
    elif isinstance(structure, float):
        return random.uniform(0, 1)
    elif isinstance(structure, bool):
        return random.choice([True, False])
    elif isinstance(structure, list):
        return [generate_random_structure(item) for item in structure]
    elif isinstance(structure, tuple):
        return tuple(generate_random_structure(item) for item in structure)
    elif isinstance(structure, dict):
        return {key: generate_random_structure(value) for key, value in structure.items()}
    else:
        raise ValueError("Unsupported data type")

# 测试代码
structure = {"ysh": 1, "b": [2, 3.0], "c": (True, False), "d": {"e": 5, "f": 6.0}}
random_structure = generate_random_structure(structure)
print(random_structure)
