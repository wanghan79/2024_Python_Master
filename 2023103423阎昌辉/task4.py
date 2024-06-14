import random


# 随机结构生成器
def generate_random_structure(depth=3, max_list_length=5, max_dict_length=3):
    if depth <= 0:
        return generate_random_value()

    structure_type = random.choice(['list', 'tuple', 'dict'])

    if structure_type == 'list':
        length = random.randint(1, max_list_length)
        return [generate_random_structure(depth - 1, max_list_length, max_dict_length) for _ in range(length)]

    if structure_type == 'tuple':
        length = random.randint(1, max_list_length)
        return tuple(generate_random_structure(depth - 1, max_list_length, max_dict_length) for _ in range(length))

    if structure_type == 'dict':
        length = random.randint(1, max_dict_length)
        return {generate_random_key(): generate_random_structure(depth - 1, max_list_length, max_dict_length) for _ in
                range(length)}


# 生成随机值
def generate_random_value():
    data_type = random.choice([int, float, str, bool])

    if data_type == int:
        return random.randint(1, 100)

    if data_type == float:
        return random.uniform(1, 100)

    if data_type == str:
        return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))

    if data_type == bool:
        return random.choice([True, False])


# 生成随机键
def generate_random_key():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))


# 示例用法
random_structure = generate_random_structure()
print(random_structure)
