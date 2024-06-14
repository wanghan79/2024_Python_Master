import random
import json
from typing import Any, List, Dict, Tuple, Union

# 定义一个通用的数据类型枚举，用于指导随机数据生成
DataGeneratorType = Union[int, float, str, bool, List, Tuple, Dict, None]

class RandomStructureGenerator:
    def __init__(self, data_type: str):
        self.data_type = data_type

    def generate(self, n: int) -> List[Any]:
        """生成 n 个随机结构的数据"""
        return [self._generate_single() for _ in range(n)]

    def _generate_single(self) -> Any:
        """生成单个随机结构的数据项"""
        if self.data_type == 'int':
            return random.randint(0, 100)
        elif self.data_type == 'float':
            return round(random.uniform(0, 100), 2)
        elif self.data_type == 'str':
            length = random.randint(1, 10)
            return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=length))
        elif self.data_type == 'bool':
            return random.choice([True, False])
        elif self.data_type == 'list':
            return [self._generate_single() for _ in range(random.randint(0, 5))]
        elif self.data_type == 'tuple':
            return tuple(self._generate_single() for _ in range(random.randint(0, 5)))
        elif self.data_type == 'dict':
            return {self._generate_single(): self._generate_single() for _ in range(random.randint(1, 5))}
        else:
            raise ValueError(f"Unsupported data type: {self.data_type}")

# 示例：使用 RandomStructureGenerator 生成随机数据
if __name__ == "__main__":
    generator = RandomStructureGenerator('list')
    random_data = generator.generate(10)
    print(json.dumps(random_data, indent=4))