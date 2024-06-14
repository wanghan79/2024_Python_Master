import random
import string

def generate_random_string(length=10):
    """生成随机字符串"""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_list(size=10, min_val=0, max_val=100):
    """生成随机整数列表"""
    return [random.randint(min_val, max_val) for _ in range(size)]

def generate_random_dict(size=10):
    """生成随机字典"""
    return {generate_random_string(5): random.randint(0, 100) for _ in range(size)}

# 示例调用
random_string = generate_random_string()
random_list = generate_random_list()
random_dict = generate_random_dict()

print(random_string)
print(random_list)
print(random_dict)
