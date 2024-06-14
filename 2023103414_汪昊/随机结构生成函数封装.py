import random
import string

def generate_random_data(data_type):
    """Generate random data based on the specified data type."""
    if data_type == "int":
        return random.randint(0, 100)
    elif data_type == "float":
        return random.uniform(0, 10000)
    elif data_type == "str":
        length = random.randint(1, 10)
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    else:
        return None

def generate_random_structure(structure):
    """Generate random data based on the structure."""
    if isinstance(structure, str):
        return generate_random_data(structure)
    elif isinstance(structure, list):
        return [generate_random_structure(item) for item in structure]
    elif isinstance(structure, tuple):
        return tuple(generate_random_structure(item) for item in structure)
    elif isinstance(structure, dict):
        return {key: generate_random_structure(value) for key, value in structure.items()}
    else:
        return None

# Example usage
data_structure = {
    "name": "str",
    "age": "int",
    "scores": ["int", "int", "int"],
    "info": {
        "city": "str",
        "email": "str"
    }
}

random_data = generate_random_structure(data_structure)
print(random_data)
