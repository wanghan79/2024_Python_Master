import random
import string

def generate_random_value(value_template):
    """Generate a random value based on the type of the input value_template."""
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

# Template data structure for student profiles
student_template = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.5,
    "courses": ["Math", "Programming", "Data Structures"],
    "contact": {
        "email": "alice@example.com",
        "phone": "123-456-7890"
    }
}

# Generate random student profiles
random_student_profiles = generate_student_profiles(5, student_template)
for profile in random_student_profiles:
    print(profile)
