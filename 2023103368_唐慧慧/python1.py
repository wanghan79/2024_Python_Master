import random

def generate_random_int():
    return random.randint(0, 100)

def generate_random_float():
    return random.random()

def generate_random_str():
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5))

def generate_random_bool():
    return random.choice([True, False])

def generate_random_value(type_hint):
    type_generators = {
        int: generate_random_int,
        float: generate_random_float,
        str: generate_random_str,
        bool: generate_random_bool
    }
    if type_hint not in type_generators:
        raise ValueError(f"Unsupported data type: {type_hint}")
    return type_generators[type_hint]()

def generate_random_structure(structure):
    if isinstance(structure, (int, float, str, bool)):
        return generate_random_value(type(structure))
    elif isinstance(structure, list):
        return [generate_random_structure(item) for item in structure]
    elif isinstance(structure, dict):
        return {key: generate_random_structure(value) for key, value in structure.items()}
    else:
        raise ValueError(f"Unsupported data structure: {structure}")

# 测试
test_structure = [1, 2.0, "string", True, [1, "abc", [3, 4]], {"a": 1, "b": [1, 2, 3, "xyz"]}]
result = generate_random_structure(test_structure)
print(result)
