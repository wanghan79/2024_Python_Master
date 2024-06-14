import random
from functools import wraps

def generate_random_value(type_hint):
    """
    生成指定类型的随机数
    """
    if type_hint is int:
        return random.randint(0, 100)
    elif type_hint is float:
        return random.uniform(0, 1)  # 使用uniform生成浮点数
    elif type_hint is str:
        return ''.join(
            random.choice('abcdefghijklmnopqrstuvwxyz')
            for _ in range(6)  # 增加字符串长度
        )
    elif type_hint is bool:
        return random.choice([True, False])
    else:
        raise ValueError(f"Unsupported data type: {type_hint}")

def recursion_decorator(func):
    """
    递归函数的修饰器
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Recursing with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@recursion_decorator
def generate_random_structure(structure):
    """
    递归生成与输入结构相同的随机数结构
    """
    if isinstance(structure, (int, float, str, bool)):
        return generate_random_value(type(structure))
    elif isinstance(structure, list):
        return [
            generate_random_structure(item)
            for item in structure
        ]
    elif isinstance(structure, dict):
        return {
            key: generate_random_structure(value)
            for key, value in structure.items()
        }
    else:
        raise ValueError(f"Unsupported data structure: {structure}")

# 测试
test_structure = [
    1, 2.0, "string", True,
    [1, 2, [3, 4]],
    {"a": 1, "b": [1, 2, 3]}
]

modified_random_structure = generate_random_structure(test_structure)
print(modified_random_structure)