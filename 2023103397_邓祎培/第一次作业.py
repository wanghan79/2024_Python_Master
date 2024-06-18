import random
import string

def generate_random_int():
    return random.randint(1, 100)

def generate_random_float():
    return random.uniform(1.0, 100.0)

def generate_random_string(length=5):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_random_structure(structure):
    if isinstance(structure, int):
        return generate_random_int()
    elif isinstance(structure, float):
        return generate_random_float()
    elif isinstance(structure, str):
        return generate_random_string(len(structure))
    elif isinstance(structure, list):
        return [generate_random_structure(item) for item in structure]
    elif isinstance(structure, dict):
        return {key: generate_random_structure(value) for key, value in structure.items()}
    else:
        return None

# 示例
input_structure = [12.5879, [26, "abc"], {"key1": 3, "key2": "def"}]
print(generate_random_structure(input_structure))
