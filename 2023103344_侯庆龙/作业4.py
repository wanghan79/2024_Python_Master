import random
import string
from faker import Faker

fake = Faker()

def random_string(length=10):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate_random_value(template_value):
    """Generate random data based on the type of the input template_value."""
    if isinstance(template_value, int):
        return random.randint(0, 100)
    elif isinstance(template_value, float):
        return round(random.uniform(0, 10000), 2)
    elif isinstance(template_value, str):
        return random_string(len(template_value))
    elif isinstance(template_value, list):
        return [generate_random_value(item) for item in template_value]
    elif isinstance(template_value, tuple):
        return tuple(generate_random_value(item) for item in template_value)
    elif isinstance(template_value, dict):
        return {key: generate_random_value(value) for key, value in template_value.items()}
    elif callable(template_value):
        return template_value()
    else:
        return None

def random_data_generator(template, count):
    """Generator that yields random data records based on the provided template data."""
    for _ in range(count):
        yield generate_random_value(template)

# Additional functions for generating random data
def random_name():
    return fake.name()

def random_email():
    return fake.email()

def random_city():
    return fake.city()

def random_major():
    majors = ['Computer Science', 'Mathematics', 'Physics', 'Biology', 'Engineering']
    return random.choice(majors)

# Template data structure
template = {
    "name": Jack,
    "age": 23,
    "scores": [10, 20, 30],
    "info": {
        "city": shanghai,
        "email": random_email
    },
    "major": random_major
}

# Generate random data records using a generator
for data in random_data_generator(template, 10):
    print(data)