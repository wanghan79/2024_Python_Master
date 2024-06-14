import random
import string

class RandomDataGenerator:
    """Class to generate random data based on a template structure."""

    def __init__(self, template):
        self.template = template

    def generate_random_value(self, template):
        """Recursively generate a random value based on the type of the input template."""
        if isinstance(template, str):
            return ''.join(random.choice(string.ascii_lowercase) for _ in range(len(template)))
        elif isinstance(template, int):
            return random.randint(18, 25)
        elif isinstance(template, float):
            return round(random.uniform(2.0, 4.0), 2)
        elif isinstance(template, list):
            return [self.generate_random_value(item) for item in template]
        elif isinstance(template, tuple):
            return tuple(self.generate_random_value(item) for item in template)
        elif isinstance(template, dict):
            return {key: self.generate_random_value(val) for key, val in template.items()}
        else:
            return None

    def generate_profiles(self, count):
        """Generate a list of random profiles based on the provided template."""
        return [self.generate_random_value(self.template) for _ in range(count)]

# Template data structure for profiles
profile_template = {
    "name": "Alice",
    "age": 23,
    "major": "Computer Science",
    "gpa": 3.5,
    "courses": ["Math", "Programming", "Data Structures"],
    "contact": {
        "email": "nenulijie",
        "phone": "1333394722"
    }
}

# Create an instance of RandomDataGenerator with the profile template
generator = RandomDataGenerator(profile_template)

# Generate random profiles
generated_profiles = generator.generate_profiles(5)
for profile in generated_profiles:
    print(profile)
