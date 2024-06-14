import random
import string


def random_value(example):

    if isinstance(example, int):
        return random.randint(0, 100)
    elif isinstance(example, float):
        return random.uniform(0.0, 100.0)
    elif isinstance(example, str):
        length = len(example) or 10
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    elif isinstance(example, list):
        return [random_value(example[0]) for _ in range(len(example) or 10)]
    elif isinstance(example, tuple):
        return tuple(random_value(item) for item in example)
    elif isinstance(example, dict):
        return {random_value(k): random_value(v) for k, v in example.items()}
    else:
        return None  # 无法识别的类型返回 None


# 测试示例
print(random_value(10))  # 随机整数
print(random_value(23.56))  # 随机浮点数
print(random_value("qwewer"))  # 随机字符串
print(random_value([1,5,7,9,35,2]))  # 随机列表
print(random_value((1,3,5,7,8,1)))  # 随机元组
print(random_value({"vjwl": 1,"fwe":2}))  # 随机字典
