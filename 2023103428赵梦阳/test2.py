import random
from typing import Any, Dict, List, Tuple, Union

class StructureRandomizer:
    def __init__(self):
        """初始化随机结构生成器"""
        pass

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

# 测试类
example_structure = {
    'key1': 1,
    'key2': [1, 2, {'key3': 3}],
    'key4': (1, 2.0, 'example')
}

randomizer = StructureRandomizer()
print(randomizer.randomize(example_structure))
