import random
import string


def generate_random_value(example):
    """
    根据给定的示例生成随机值。

    :param example: 示例数据，可以是任何类型
    :return: 生成的随机数据
    """
    if isinstance(example, int):
        return random.randint(0, 100)
    elif isinstance(example, float):
        return random.uniform(0.0, 100.0)
    elif isinstance(example, str):
        length = len(example) or 10
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    elif isinstance(example, list):
        return [generate_random_value(example[0]) for _ in range(len(example) or 10)]
    elif isinstance(example, tuple):
        return tuple(generate_random_value(item) for item in example)
    elif isinstance(example, dict):
        return {generate_random_value(k): generate_random_value(v) for k, v in example.items()}
    else:
        return None  # 无法识别的类型返回 None

def random_value_decorator(example):
    def decorator(func):
        def wrapper(*args, **kwargs):
            random_value = generate_random_value(example)
            return func(random_value, *args, **kwargs)
        return wrapper
    return decorator

@random_value_decorator(10)
def example_function(value):
    return value

# 测试示例
print(example_function())
print(example_function())
