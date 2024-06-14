# coding=utf-8
import random
import string

def generate_random_values(data):
    if isinstance(data, int):
        return random.randint(0, 100)
    elif isinstance(data, float):
        return random.uniform(0, 100)
    elif isinstance(data, str):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(len(data)))
    elif isinstance(data, list):
        return [generate_random_values(item) for item in data]
    elif isinstance(data, tuple):
        return tuple(generate_random_values(item) for item in data)
    elif isinstance(data, dict):
        return {key: generate_random_values(value) for key, value in data.items()}
    else:
        return None

# 测试示例
original_data = {
    "name": "Alice",
    "age": 30,
    "major": "computer",  # 修正拼写错误
    "scores": [90, 85, 88],
    "info": {
        "city": "New York",
        "email": "alice@example.com",
        "roommates": ["tom", "liming", "david"]  # 修正拼写错误
    }
}

# 生成并打印随机数据
random_data_list = [generate_random_values(original_data) for _ in range(2)]
for data in random_data_list:
    print(data)
