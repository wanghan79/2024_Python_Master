import random
from typing import Any, Dict, List, Tuple, Union

def create_random_structure(template: Any) -> Any:
    """生成与传入模板结构相同的随机数结构"""
    if isinstance(template, dict):
        return {k: create_random_structure(v) for k, v in template.items()}
    elif isinstance(template, list):
        return [create_random_structure(item) for item in template]
    elif isinstance(template, tuple):
        return tuple(create_random_structure(item) for item in template)
    elif isinstance(template, int):
        return random.randint(0, 100)
    elif isinstance(template, float):
        return random.uniform(0, 100)
    elif isinstance(template, str):
        return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    else:
        return None

# 测试函数
example_structure = {
    'key1': 1,
    'key2': [1, 2, {'key3': 3}],
    'key4': (1, 2.0, 'example')
}

print(create_random_structure(example_structure))
