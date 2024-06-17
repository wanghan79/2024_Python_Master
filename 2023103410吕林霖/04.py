import random
import time
from functools import wraps

# 定义修饰器，用于记录函数运行时间
def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end-start:.6f} seconds to run.")
        return result
    return wrapper

# 定义一个生成随机数的类
class RandomGenerator:
    def __init__(self):
        pass

    def random_int(self, low, high):
        return random.randint(low, high)

    def random_float(self, low, high, precision=2):
        return round(random.uniform(low, high), precision)

    def random_choice(self, seq):
        return random.choice(seq)

# 定义一个迭代器类，用于生成嵌套结构的随机数
class NestedRandomIterator:
    def __init__(self, structure, generator):
        self.structure = structure
        self.generator = generator

    def __iter__(self):
        return self

    def __next__(self):
        return self._generate_random_structure(self.structure)

    def _generate_random_structure(self, structure):
        if isinstance(structure, int):
            return self.generator.random_int(0, structure)
        elif isinstance(structure, float):
            return self.generator.random_float(0, structure)
        elif isinstance(structure, str):
            return self.generator.random_choice(structure)
        elif isinstance(structure, list):
            return [self._generate_random_structure(item) for item in structure]
        elif isinstance(structure, tuple):
            return tuple(self._generate_random_structure(item) for item in structure)
        elif isinstance(structure, dict):
            return {key: self._generate_random_structure(value) for key, value in structure.items()}
        else:
            raise ValueError("Unsupported structure type")

# 定义一个生成随机嵌套结构的类
class NestedRandomGenerator:
    def __init__(self):
        self.generator = RandomGenerator()

    @timing
    def generate(self, structure):
        iterator = NestedRandomIterator(structure, self.generator)
        return next(iterator)

# 使用示例
if __name__ == "__main__":
    nested_structure = [10, [5.0, "abc"], {"key1": 3, "key2": [1, 2, 3]}]
    generator = NestedRandomGenerator()
    random_structure = generator.generate(nested_structure)
    print(random_structure)