import random
import string
from faker import Faker

fake_generator = Faker()

def generate_random_string(length=10):
    """返回指定长度的随机小写字母字符串"""
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate_structure(template):
    """根据输入模板的类型和结构生成随机数据"""
    if isinstance(template, int):
        return random.randint(0, 100)
    elif isinstance(template, float):
        return random.uniform(0, 10000)
    elif isinstance(template, str):
        return generate_random_string(len(template))
    elif isinstance(template, list):
        return [generate_structure(item) for item in template]
    elif isinstance(template, tuple):
        return tuple(generate_structure(item) for item in template)
    elif isinstance(template, dict):
        return {key: generate_structure(value) for key, value in template.items()}
    else:
        return None

def data_generator(template, quantity):
    """根据提供的模板数据生成随机数据记录的生成器"""
    for _ in range(quantity):
        yield generate_structure(template)

# 模板数据结构
template_data = {
    "name": "Bob",
    "age": 25,
    "scores": [15, 25, 35],
    "info": {
        "city": "Los Angeles",
        "email": "bob@example.com"
    },
    "specialization": "jishuxitong"
}

# 生成基于修改后模板的随机数据记录
generated_data = data_generator(template_data, 10)
for data in generated_data:
    print(data)

# 使用生成器生成随机数据记录
for data in data_generator(template_data, 10):
    print(data)
