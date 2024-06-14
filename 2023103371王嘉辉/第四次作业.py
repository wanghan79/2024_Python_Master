import random
import string
from faker import Faker

fake = Faker()

def generate_random_str(size=10):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(size))

def create_random_data(structure):
    if isinstance(structure, int):
        return random.randint(0, 100)
    elif isinstance(structure, float):
        return random.uniform(0, 10000)
    elif isinstance(structure, str):
        return generate_random_str(len(structure))
    elif isinstance(structure, list):
        return [create_random_data(item) for item in structure]
    elif isinstance(structure, tuple):
        return tuple(create_random_data(item) for item in structure)
    elif isinstance(structure, dict):
        return {key: create_random_data(value) for key, value in structure.items()}
    else:
        return None

def generate_random_records(template, num_records):
    for _ in range(num_records):
        yield create_random_data(template)


data_template = {
    "full_name": fake.name(),
    "numeric_value": 18,
    "sequence": [10, 20, 30],
    "details": {
        "location": "New York",
        "contact": "alice@example.com"
    },
    "field_of_study": "computer science"
}

for record in generate_random_records(data_template, 10):
    print(record)
