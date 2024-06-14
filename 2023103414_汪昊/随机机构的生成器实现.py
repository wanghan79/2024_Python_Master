import random
import string

def generate_random_data(data_type):
    """Generate random data based on the specified data type."""
    if data_type == "int":
        while True:
            yield random.randint(0, 100)
    elif data_type == "float":
        while True:
            yield random.uniform(0, 10000)
    elif data_type == "str":
        while True:
            length = random.randint(1, 10)
            yield ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    else:
        yield None

def generate_random_structure(structure):
    """Generate random data based on the structure."""
    if isinstance(structure, str):
        yield from generate_random_data(structure)
    elif isinstance(structure, list):
        yield [data for data in generate_random_structure(item) for item in structure]
    elif isinstance(structure, tuple):
        yield tuple(data for data in generate_random_structure(item) for item in structure)
    elif isinstance(structure, dict):
        yield {key: data for key, data in zip(structure.keys(), generate_random_structure(structure.values()))}
    else:
        yield None

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

random_data_generator = generate_random_structure(data_structure)
for _ in range(10):
    random_data = next(random_data_generator)
    print(random_data)
