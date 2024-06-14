import random


# 使用函数级封装生成随机数
def generate_random_data(data_structure):
    if isinstance(data_structure, list):
        return [generate_random_data(item) for item in data_structure]
    elif isinstance(data_structure, tuple):
        return tuple(generate_random_data(item) for item in data_structure)
    elif isinstance(data_structure, dict):
        return {key: generate_random_data(value) for key, value in data_structure.items()}
    else:
        return generate_random_value(data_structure)


# 生成随机值
def generate_random_value(data_type):
    if data_type == int:
        return random.randint(1, 100)
    elif data_type == float:
        return random.uniform(1, 100)
    elif data_type == str:
        return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    elif data_type == bool:
        return random.choice([True, False])
    else:
        return None


# 示例用法
data_structure = [int, [str, bool], {'key': float}]
random_data = generate_random_data(data_structure)
print(random_data)
