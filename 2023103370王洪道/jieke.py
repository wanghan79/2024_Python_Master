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

# Template data structure for employee records
employee_template = {
    "name": fake.name(),  # Random employee name
    "age": random.randint(18, 65),  # Random age between 18 and 65
    "department": random.choice(["HR", "IT", "Finance", "Operations"]),  # Random department
    "skills": [fake.job(), fake.job(), fake.job()],  # Random skills list
    "contact": {
        "email": fake.email(),  # Random email address
        "phone": fake.phone_number(),  # Random phone number
        "address": fake.address()  # Random address
    },
    "salary": random.uniform(30000, 120000)  # Random salary between $30,000 and $120,000
}

# Generate random employee records based on the modified template
def generate_employee_records(count, template):
    return [random_structure(template) for _ in range(count)]

# Generate and print random employee records
employee_records = generate_employee_records(5, employee_template)
for idx, employee in enumerate(employee_records, start=1):
    print(f"Employee {idx}:")
    for key, value in employee.items():
        print(f"{key}: {value}")
    print()

# Generate random employee records using a generator
print("Generating employee records using a generator:")
for idx, employee in enumerate(random_data_generator(employee_template, 5), start=1):
    print(f"Employee {idx}:")
    for key, value in employee.items():
        print(f"{key}: {value}")
    print()
