'''
期末作业：生成随机数据
'''
import random
import string

def random_string(length=10):
    """生成给定字长"""
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def random_structure(template):
    """生成随机数据"""
    if isinstance(template, int):
        return random.randint(0, 100)
    elif isinstance(template, float):
        return round(random.uniform(0, 10000), 2)
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
    for _ in range(count):
        yield random_structure(template)

# Template data structure
same_data = {
    "name": "Bob",  # 修改姓名为"Bob"
    "age": 25,  # 修改年龄为25岁
    "scores": [15, 25, 35],  # 修改分数列表
    "info": {
        "city": "Los Angeles",  # 修改城市为"Los Angeles"
        "email": "bob@example.com"  # 修改邮箱
    },
    "zhuanye": "jishuxitong"  # 修改专业
}

# Generate random data records using a generator
for data in random_data_generator(same_data, 10):
    print(data)
