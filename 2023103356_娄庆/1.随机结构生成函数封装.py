import random
import string
from typing import Any, Callable, Generator

def randomize_value() -> Any:
    """生成随机值的生成器函数"""
    yield random.randint(1, 100)  # 随机整数
    yield random.uniform(1.0, 100.0)  # 随机浮点数
    yield ''.join(random.choices(string.ascii_letters + string.digits, k=5))  # 随机字符串
    yield None  # None值
    yield True  # 布尔值True
    yield False  # 布尔值False

def randomize_structure(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """随机化结构的装饰器函数"""
    def wrapper(input_para: Any) -> Any:
        if isinstance(input_para, int):
            return random.randint(1, 100)
        elif isinstance(input_para, float):
            return random.random()
        elif isinstance(input_para, str):
            return ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        elif isinstance(input_para, list):
            return [randomize_structure(lambda x: x)(item) for item in input_para]
        elif isinstance(input_para, tuple):
            return tuple(randomize_structure(lambda x: x)(item) for item in input_para)
        elif isinstance(input_para, dict):
            return {key: randomize_structure(lambda x: x)(value) for key, value in input_para.items()}
        else:
            return next(randomize_value())
    return wrapper

# 示例调用
if __name__ == '__main__':
    input_structure = [
        {"key1": [1, 2], "key2": (3, 4)},
        (5, 6),
        [7, 8]
    ]
    b = [1, 1.2, "djgjn", input_structure]
    for i in b:
        randomized_structure = randomize_structure(lambda x: x)(i)
        print(randomized_structure)
