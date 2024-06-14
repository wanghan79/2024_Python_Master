import random
import string

def create_random_value(data_template):
    """Generate a random value based on the type of the input data_template."""
    if isinstance(data_template, str):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(len(data_template)))
    elif isinstance(data_template, int):
        return random.randint(18, 25)
    elif isinstance(data_template, float):
        return round(random.uniform(2.0, 4.0), 2)
    elif isinstance(data_template, list):
        return [create_random_value(item) for item in data_template]
    elif isinstance(data_template, tuple):
        return tuple(create_random_value(item) for item in data_template)
    elif isinstance(data_template, dict):
        return {key: create_random_value(val) for key, val in data_template.items()}
    else:
        return None

def create_random_profiles(count, profile_structure):
    """Generate a list of random profiles based on the provided profile structure."""
    return [create_random_value(profile_structure) for _ in range(count)]

# Template data structure for profiles
profile_template = {
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

# Generate random profiles
generated_profiles = create_random_profiles(5, profile_template)
for profile in generated_profiles:
    print(profile)
