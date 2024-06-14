'''
第二次作业：封装类
'''
import random

class RandomNumberGenerator:
    def __init__(self, rand_type, rand_range, rand_size):
        self.rand_type = rand_type
        self.rand_range = rand_range
        self.rand_size = rand_size
        self.validate_params()

    def validate_params(self):
        # 检查 'range' 参数是否有效
        if not (isinstance(self.rand_range, (list, tuple)) and len(self.rand_range) == 2 and self.rand_range[0] <= self.rand_range[1]):
            raise ValueError("'Range '必须是一个包含两个元素的列表或元组，其中第一个元素小于或等于第二个元素")

        # 检查 'size' 参数是否有效
        if not (isinstance(self.rand_size, int) and self.rand_size > 0):
            raise ValueError("'size' 需是 positive integer")

    def generate(self):
        # 生成随机数列表
        if self.rand_type == 'int':
            return [random.randint(self.rand_range[0], self.rand_range[1]) for _ in range(self.rand_size)]
        elif self.rand_type == 'float':
            return [random.uniform(self.rand_range[0], self.rand_range[1]) for _ in range(self.rand_size)]
        else:
            raise ValueError("示例只包含: 'int', 'float'")

# 示例化并使用该类
params1 = {'rand_type': 'int', 'rand_range': (1, 10), 'rand_size': 4}
params2 = {'rand_type': 'float', 'rand_range': (0.0, 50.0), 'rand_size': 5}

generator1 = RandomNumberGenerator(**params1)
random_integers = generator1.generate()

generator2 = RandomNumberGenerator(**params2)
random_floats = generator2.generate()

# 输出结果
print("随机整数:", random_integers)
print("随机浮点数:", random_floats)

