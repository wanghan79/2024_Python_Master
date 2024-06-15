import random
import string

def random_value():
    return random.choice([
        random.randint(1, 100),  # 随机整数
        random.uniform(1.0, 100.0),  # 随机浮点数
        ''.join(random.choices(string.ascii_letters + string.digits, k=5)),  # 随机字符串
        None,
        True,
        False
    ])

def random_structure(structure, *args):
    if isinstance(structure, list):
        return [random_structure(item, *args) for item in structure]
    elif isinstance(structure, tuple):
        return tuple(random_structure(item, *args) for item in structure)
    elif isinstance(structure, dict):
        return {key: random_structure(value, *args) for key, value in structure.items()}
    else:
        return random_value()

input = [
    {"key1": ['one', 'two'], "key2": (1, 2)},
    (3, 4),
    [5, 6]
]

# 生成随机结构
output = random_structure(input)
print(output)
