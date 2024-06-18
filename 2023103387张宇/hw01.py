
import random
import string


def generate_random_structure(*args, **kwargs):
    # 从参数中提取数量范围，如果没有提供，使用默认值
    num_min = kwargs.get('num_min', 1)
    num_max = kwargs.get('num_max', 10)

    if num_min > num_max:
        raise ValueError("num_min should be less than or equal to num_max")

    # 生成随机数量
    num_count = random.randint(num_min, num_max)

    # 生成随机数范围
    value_min = kwargs.get('value_min', 0)
    value_max = kwargs.get('value_max', 100)

    if value_min > value_max:
        raise ValueError("value_min should be less than or equal to value_max")

    # 生成随机字符串长度范围
    str_min_len = kwargs.get('str_min_len', 5)
    str_max_len = kwargs.get('str_max_len', 10)

    if str_min_len > str_max_len:
        raise ValueError("str_min_len should be less than or equal to str_max_len")

    # 用于生成随机字符串的字符集
    use_uppercase = kwargs.get('use_uppercase', True)
    use_lowercase = kwargs.get('use_lowercase', True)
    use_digits = kwargs.get('use_digits', True)
    use_punctuation = kwargs.get('use_punctuation', False)

    # 构建字符集
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be enabled for string generation")

    # 生成随机数和随机字符串
    random_elements = []
    for _ in range(num_count):
        if random.choice([True, False]):
            # 生成随机数
            random_elements.append(random.randint(value_min, value_max))
        else:
            # 生成随机字符串
            str_len = random.randint(str_min_len, str_max_len)
            random_string = ''.join(random.choice(characters) for _ in range(str_len))
            random_elements.append(random_string)

    # 随机选择生成的结构类型
    structure_type = random.choice(['list', 'dict','tuple'])

    if structure_type == 'list':
        # 生成列表
        random_structure = random_elements
    elif structure_type == 'tuple':
        random_structure = tuple(random_elements)
    else:
        # 生成字典，键为随机生成的字符串，值为随机元素
        random_structure = {f'key_{i}': random_elements[i] for i in range(num_count)}

    return random_structure


# 示例调用
random_structure = generate_random_structure(num_min=5, num_max=15, value_min=10, value_max=50, str_min_len=5,
                                             str_max_len=15, use_punctuation=True)
print(random_structure)
