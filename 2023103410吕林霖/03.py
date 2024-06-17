import random
import time
from functools import wraps

def stats_decorator(func):
    """
    统计方法修饰器,用于记录函数的运行时间和调用次数。
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        wrapper.call_count += 1
        wrapper.total_time += (end_time - start_time)
        print(f"Function {func.__name__} called {wrapper.call_count} times. Average execution time: {wrapper.total_time / wrapper.call_count:.6f} seconds.")
        return result
    wrapper.call_count = 0
    wrapper.total_time = 0.0
    return wrapper

class RandomStructureGenerator:
    """
    随机结构生成器类。
    """

    def __init__(self, data_type="int", range_start=0, range_end=100):
        """
        初始化生成器。
        """
        self.data_type = data_type
        self.range_start = range_start
        self.range_end = range_end

    def __iter__(self):
        """
        使生成器可迭代。
        """
        return self

    @stats_decorator
    def __next__(self):
        """
        生成下一个随机数据。
        """
        if self.data_type == "int":
            return random.randint(self.range_start, self.range_end)
        elif self.data_type == "float":
            return random.uniform(self.range_start, self.range_end)
        elif self.data_type == "str":
            return "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(random.randint(1, 10)))
        else:
            raise ValueError("不支持的数据类型")

# 示例用法
generator = RandomStructureGenerator(data_type="int", range_start=1, range_end=10)

# 迭代生成 5 个随机整数
for _ in range(5):
    print(next(generator))

# 生成一个包含 10 个随机浮点数的列表
random_list = [next(generator) for _ in range(10)]
print(f"随机列表: {random_list}")

# 生成一个包含 5 个随机字符串的字典
random_dict = {str(i): next(generator) for i in range(5)}
print(f"随机字典: {random_dict}")