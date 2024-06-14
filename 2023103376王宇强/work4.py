import random
import string

class RandomStructureGenerator:
    def __init__(self, depth=3, int_range=(0, 100), float_range=(0.0, 100.0), str_len=8):
        self.depth = depth
        self.int_range = int_range
        self.float_range = float_range
        self.str_len = str_len
        self.types = [self.random_int, self.random_float, self.random_str, self.random_list, self.random_tuple, self.random_dict]

    def random_int(self):
        return random.randint(*self.int_range)

    def random_float(self):
        return random.uniform(*self.float_range)

    def random_str(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=self.str_len))

    def random_list(self, depth):
        return [self.random_element(depth - 1) for _ in range(random.randint(1, 5))]

    def random_tuple(self, depth):
        return tuple(self.random_element(depth - 1) for _ in range(random.randint(1, 5)))

    def random_dict(self, depth):
        return {self.random_str(): self.random_element(depth - 1) for _ in range(random.randint(1, 5))}

    def random_element(self, depth):
        if depth <= 0:
            return random.choice([self.random_int(), self.random_float(), self.random_str()])
        return random.choice(self.types)(depth)

    def generate(self):
        return self.random_element(self.depth)

# 测试随机结构生成器
generator = RandomStructureGenerator(depth=3, int_range=(10, 50), float_range=(10.0, 50.0), str_len=5)
random_structure = generator.generate()
print(random_structure)
