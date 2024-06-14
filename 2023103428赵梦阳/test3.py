import random
from typing import Any, Dict, List, Tuple, Union
from functools import wraps

def count_calls(func):
    """修饰器：统计函数调用次数"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        wrapper.calls += 1
        return func(self, *args, **kwargs)
    wrapper.calls = 0
    return wrapper

class StructureRandomizer:
    def __init__(self):
        """初始化随机结构生成器"""
        self._generate_calls = 0

    @count_calls
    def randomize(self, template: Any) -> Any:
        """生成与传入模板结构相同的随机数结构"""
        if isinstance(template, dict):
            return {k: self.randomize(v) for k, v in template.items()}
        elif isinstance(template, list):
            return [self.randomize(item) for item in template]
        elif isinstance(template, tuple):
            return tuple(self.randomize(item) for item in template)
        elif isinstance(template, int):
            return random.randint(0, 100)
        elif isinstance(template, float):
            return random.uniform(0, 100)
        elif isinstance(template, str):
            return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
        else:
            return None

    def get_call_count(self) -> int:
        """返回生成随机结构方法的调用次数"""
        return self.randomize.calls

# 测试类
example_structure = {
    'key1': 1,
    'key2': [1, 2, {'key3': 3}],
    'key4': (1, 2.0, 'example')
}

randomizer = StructureRandomizer()
print(randomizer.randomize(example_structure))
print(f"Randomize method called: {randomizer.get_call_count()} times")
