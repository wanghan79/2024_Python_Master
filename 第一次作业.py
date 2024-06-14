# coding=utf-8
import random
import string


def generate_random_data(data):
    if isinstance(data, int):
        return random.randint(0, 100)
    elif isinstance(data, float):
        return random.uniform(0, 100)
    elif isinstance(data, str):
        return ''.join(random.choice(string.ascii_lowercase)for _ in range(len(data)))
    elif isinstance(data, list):
        return [generate_random_data(item) for item in data]
    elif isinstance(data, tuple):
        return tuple(generate_random_data(item) for item in data)
    elif isinstance(data, dict):
        return {key: generate_random_data(value) for key, value in data.items()}
    else:
        return None

# 测试示例
original_data = {
    "name": "Alice",
    "age": 30,
    "majors":"computer",
    "scores": [90, 85, 88],
    "info": {
        "city": "New York",
        "email": "alice@example.com",
        "rommtoor":["tom","liming","david"]
    }
}

# 打印
random_list = [generate_random_data(original_data) for _ in range(2)]#生成随机数量
for random_number in random_list:
    print(random_number)
