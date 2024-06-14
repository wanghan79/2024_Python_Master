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
same_data= {
    "name": "Bob",  # 修改姓名为"Bob"
    "age": 25,  # 修改年龄为25岁
    "scores": [15, 25, 35],  # 修改分数列表
    "info": {
        "city": "Los Angeles",  # 修改城市为"Los Angeles"
        "email": "bob@example.com"  # 修改邮箱
    },
    "zhuanye": "jishuxitong"  # 修改专业
}

# Generate random data records based on the modified template
random_data = generate_original_data(10, same_data)
for data in random_data:
    print(data)

# Generate random data records using a generator
for data in random_data_generator(same_data, 10):
    print(data)
