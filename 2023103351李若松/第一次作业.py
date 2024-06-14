import random
import string

def generate_random_data(data):
    """Generate random data based on the type and structure of the input data."""
    if isinstance(data, int):
        return random.randint(0, 100)
    elif isinstance(data, float):
        return random.uniform(0, 10000)
    elif isinstance(data, str):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(len(data)))
    elif isinstance(data, list):
        return [generate_random_data(item) for item in data]
    elif isinstance(data, tuple):
        return tuple(generate_random_data(item) for item in data)
    elif isinstance(data, dict):
        return {key: generate_random_data(value) for key, value in data.items()}
    else:
        return None

def generate_original_data(num, template_data):
    """Generate a list of random data records based on the provided template data."""
    return [generate_random_data(template_data) for _ in range(num)]

# Template data structure
same_data = {
    "name": "Alice",
    "age": 18,
    "scores": [10, 20, 30],
    "info": {
        "city": "New York",
        "email": "alice@example.com"
    },
    "zhuanye": "jisuanji"
}

# Generate random data records
random_data = generate_original_data(10, same_data)
for data in random_data:
    print(data)