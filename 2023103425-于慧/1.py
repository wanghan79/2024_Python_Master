import random
import string

def generate_random_value(value_type):
    if value_type == int:
        return random.randint(0, 100)
    elif value_type == float:
        return random.uniform(0, 100)
    elif value_type == str:
        # 使用 random.sample 来生成一个随机字符串
        return ''.join(random.sample(string.ascii_letters + string.digits, 8))
    elif value_type == bool:
        return random.choice([True, False])
    else:
        raise ValueError("Unsupported value type: {}".format(value_type))

def generate_random_structure(structure):
    if isinstance(structure, dict):
        return {k: generate_random_structure(v) for k, v in structure.items()}
    elif isinstance(structure, list):
        return [generate_random_structure(elem) for elem in structure]
    elif isinstance(structure, tuple):
        return tuple(generate_random_structure(elem) for elem in structure)
    elif isinstance(structure, set):
        return {generate_random_structure(elem) for elem in structure}
    elif isinstance(structure, type):  # Check if it's a type
        return generate_random_value(structure)
    else:
        raise ValueError("Unsupported structure type: {}".format(type(structure)))

# Example usage
input_structure = {
    'a': int,
    'b': [float, str],
    'c': {'d': bool, 'e': int},
    'f': (str, float)
}

print(generate_random_structure(input_structure))