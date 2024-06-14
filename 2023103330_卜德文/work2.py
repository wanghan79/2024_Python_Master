import random
import string


class RandomValueGenerator:
    def __init__(self):
        pass

    def generate(self, example):

        if isinstance(example, int):
            return random.randint(0, 100)
        elif isinstance(example, float):
            return random.uniform(0.0, 100.0)
        elif isinstance(example, str):
            length = len(example) or 10
            return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        elif isinstance(example, list):
            return [self.generate(example[0]) for _ in range(len(example) or 10)]
        elif isinstance(example, tuple):
            return tuple(self.generate(item) for item in example)
        elif isinstance(example, dict):
            return {self.generate(k): self.generate(v) for k, v in example.items()}
        else:
            return None  # 无法识别的类型返回 None


# 测试示例
rvg = RandomValueGenerator()
print(rvg.generate(10))  # 随机整数
print(rvg.generate(10.5))  # 随机浮点数
print(rvg.generate("dfbaerg"))  # 随机字符串
print(rvg.generate([1,3,5,6,78,9]))  # 随机列表
print(rvg.generate((1,4,6,8,9,2,1,7)))  # 随机元组
print(rvg.generate({"erg": 1,"erg":2}))  # 随机字典
