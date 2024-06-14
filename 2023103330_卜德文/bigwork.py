import random
import string


def generate_random_value(example):


    if isinstance(example, int):
        return random.randint(0, 100)
    elif isinstance(example, float):
        return random.uniform(0.0, 100.0)
    elif isinstance(example, str):
        length = len(example) or 10
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    elif isinstance(example, list):
        return [generate_random_value(example[0]) for _ in range(len(example) or 10)]
    elif isinstance(example, tuple):
        return tuple(generate_random_value(item) for item in example)
    elif isinstance(example, dict):
        return {generate_random_value(k): generate_random_value(v) for k, v in example.items()}
    else:
        return None  # 无法识别的类型返回 None


def random_value_generator(example):

    while True:
        yield generate_random_value(example)


# 测试示例
gen = random_value_generator(10)
for _ in range(5):
    print(next(gen))

gen = random_value_generator("hello")
for _ in range(5):
    print(next(gen))
