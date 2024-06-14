import random
import string

class RandomStructureGenerator:
    def __init__(self, string_length=10, list_size=10, dict_size=10, min_val=0, max_val=100):
        self.string_length = string_length
        self.list_size = list_size
        self.dict_size = dict_size
        self.min_val = min_val
        self.max_val = max_val

    def generate_random_string(self):
        """生成随机字符串"""
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(self.string_length))

    def generate_random_list(self):
        """生成随机整数列表"""
        return [random.randint(self.min_val, self.max_val) for _ in range(self.list_size)]

    def generate_random_dict(self):
        """生成随机字典"""
        return {self.generate_random_string(): random.randint(0, 100) for _ in range(self.dict_size)}

# 示例调用
generator = RandomStructureGenerator()
print(generator.generate_random_string())
print(generator.generate_random_list())
print(generator.generate_random_dict())
