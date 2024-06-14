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

# Template data structure for testing
test_template = {
    "name": fake.name(),
    "age": 30,
    "address": {
        "city": fake.city(),
        "street": fake.street_address(),
        "zipcode": fake.zipcode()
    },
    "phone_numbers": [fake.phone_number(), fake.phone_number()],
    "scores": [100, 200, 300],
    "info": {
        "email": fake.email(),
        "website": fake.url()
    },
    "tags": ("python", "data", "test"),
    "is_active": True
}

# Generate random data records using a generator
for data in random_data_generator(test_template, 5):
    print(data)
