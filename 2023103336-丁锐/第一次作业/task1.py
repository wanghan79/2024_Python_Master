import random
import string

def random_value():
    return random.choice([
        random.randint(1, 100),  # 随机整数
        random.uniform(1.0, 100.0),  # 随机浮点数
        ''.join(random.choices(string.ascii_letters + string.digits, k=5)),  # 随机字符串
        None,  # None值
        True,  # 布尔值True
        False  # 布尔值False
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

# 示例输入结构
input_structure = [
    {"key1": [1, 2], "key2": (3, 4)},
    (5, 6),
    [7, 8]
]

# 生成随机结构
randomized_structure = random_structure(input_structure)
print(randomized_structure)
