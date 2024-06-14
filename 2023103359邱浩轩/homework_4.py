import random
import string
from faker import Faker

fake = Faker()

def random_string(length=10):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def random_structure(template):
    """Generate random data based on the type and structure of the input template."""
    if isinstance(template, int):
        return random.randint(0, 100)
    elif isinstance(template, float):
        return random.uniform(0, 10000)
    elif isinstance(template, str):
        return random_string(len(template))
    elif isinstance(template, list):
        return [random_structure(item) for item in template]
    elif isinstance(template, tuple):
        return tuple(random_structure(item) for item in template)
    elif isinstance(template, dict):
        return {key: random_structure(value) for key, value in template.items()}
    else:
        return None

def random_data_generator(template, count):
    """Generator that yields random data records based on the provided template data."""
    for _ in range(count):
        yield random_structure(template)

# Template data structure
sample_data = {
    "company": fake.company(),
    "price": 99.99,
    "tags": ["sale", "discount", "clearance"],
    "details": {
        "location": "San Francisco",
        "contact_email": "info@company.com"
    },
    "category": "electronics"
}

# Generate random data records using a generator
for data in random_data_generator(sample_data, 10):
    print(data)
