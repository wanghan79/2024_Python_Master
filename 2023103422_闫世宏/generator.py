import random

def random_structure_generator(structure):
    if isinstance(structure, int):
        yield random.randint(0, 100)
    elif isinstance(structure, float):
        yield random.uniform(0, 1)
    elif isinstance(structure, bool):
        yield random.choice([True, False])
    elif isinstance(structure, list) or isinstance(structure, tuple):
        for item in structure:
            yield from random_structure_generator(item)
    elif isinstance(structure, dict):
        for key, value in structure.items():
            yield key, random_structure_generator(value)
    else:
        raise ValueError("Unsupported data type")

# 测试代码
structure = {"a": 1, "b": [2, 3.0], "c": (True, False), "d": {"e": 5, "f": 6.0}}
generator = random_structure_generator(structure)
for item in generator:
    print(item)
