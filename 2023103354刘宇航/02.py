import random
import string

class RandomStructureGenerator:
    def __init__(self, seed=None):
        if seed is not None:
            random.seed(seed)
    
    def random_string(self, length=10):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))
    
    def random_integer(self, min_val=0, max_val=100):
        return random.randint(min_val, max_val)
    
    def random_list(self, length=10, min_val=0, max_val=100):
        return [self.random_integer(min_val, max_val) for _ in range(length)]
    
    def random_dict(self, num_keys=5, min_val=0, max_val=100):
        keys = [self.random_string(5) for _ in range(num_keys)]
        return {key: self.random_integer(min_val, max_val) for key in keys}

# 示例调用
if __name__ == "__main__":
    generator = RandomStructureGenerator(seed=42)
    
    print("随机字符串:", generator.random_string(15))
    print("随机整数:", generator.random_integer(10, 50))
    print("随机列表:", generator.random_list(8, 1, 10))
    print("随机字典:", generator.random_dict(3, 1, 20))