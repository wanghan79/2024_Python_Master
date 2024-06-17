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
        print(f"Function {func.__name__} took {end - start:.6f} seconds to run.")
        return result

    return wrapper


# 定义一个迭代器类，用于生成随机整数
class RandomIntegers:
    def __init__(self, low, high, count):
        self.low = low
        self.high = high
        self.count = count
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.count:
            self.current += 1
            return random.randint(self.low, self.high)
        else:
            raise StopIteration


# 定义一个生成器函数，用于生成随机浮点数
def random_floats(low, high, count, precision=2):
    for _ in range(count):
        yield round(random.uniform(low, high), precision)


# 定义一个随机结构生成类
class RandomStructGenerator:
    def __init__(self):
        pass

    @timing
    def generate_random_integers(self, low, high, count):
        return list(RandomIntegers(low, high, count))

    @timing
    def generate_random_floats(self, low, high, count, precision=2):
        return list(random_floats(low, high, count, precision))


# 使用示例
if __name__ == "__main__":
    generator = RandomStructGenerator()

    int_list = generatoar.generate_random_integers(1, 100, 10)
    print(int_list)

    float_list = generator.generate_random_floats(0, 1, 5, 3)
    print(float_list)