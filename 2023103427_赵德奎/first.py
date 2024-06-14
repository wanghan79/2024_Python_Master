import random
import string
from faker import Faker

fake = Faker()

def generate_random_value(value_template):
    if isinstance(value_template, str):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(len(value_template)))
    elif isinstance(value_template, int):
        return random.randint(18, 25)
    elif isinstance(value_template, float):
        return round(random.uniform(2.0, 4.0), 2)
    elif isinstance(value_template, list):
        return [generate_random_value(item) for item in value_template]
    elif isinstance(value_template, tuple):
        return tuple(generate_random_value(item) for item in value_template)
    elif isinstance(value_template, dict):
        return {key: generate_random_value(value) for key, value in value_template.items()}
    else:
        return None

def generate_student_profiles(num_records, template_data):
    """Generate a list of random student profiles based on the provided template data."""
    return [generate_random_value(template_data) for _ in range(num_records)]

# New template for student profiles
student_template = {
    "name": fake.name(),
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.5,
    "courses": ["Math", "Programming", "Data Structures"],
    "contact": {
        "email": fake.email(),
        "phone": fake.phone_number()
    },
    "graduation_year": 2024,
    "address": {
        "city": fake.city(),
        "street": fake.street_address(),
        "zipcode": fake.zipcode()
    }
}

# Generate random student profiles
random_student_profiles = generate_student_profiles(5, student_template)
for profile in random_student_profiles:
    print(profile)
