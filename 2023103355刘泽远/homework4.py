import random
import string
import time
from functools import wraps

class Data:
    def __init__(self, integer_value, double_value, string_value, boolean_value):
        self.integer_value = integer_value
        self.double_value = double_value
        self.string_value = string_value
        self.boolean_value = boolean_value

    def __repr__(self):
        return (f"Data(integer_value={self.integer_value}, double_value={self.double_value}, "
                f"string_value='{self.string_value}', boolean_value={self.boolean_value})")

class MethodStats:
    def __init__(self):
        self.call_count = 0
        self.total_time = 0.0

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self.call_count += 1
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            self.total_time += (end_time - start_time)
            return result
        return wrapper

    def get_stats(self):
        return {
            'call_count': self.call_count,
            'total_time': self.total_time,
            'average_time': self.total_time / self.call_count if self.call_count > 0 else 0
        }

class RandomDataGenerator:
    stats = MethodStats()

    def __init__(self, int_range=(0, 100), double_range=(0.0, 1.0), string_length=10):
        self.int_range = int_range
        self.double_range = double_range
        self.string_length = string_length

    @stats
    def generate_data(self):
        integer_value = random.randint(self.int_range[0], self.int_range[1])
        double_value = random.uniform(self.double_range[0], self.double_range[1])
        string_value = ''.join(random.choices(string.ascii_letters + string.digits, k=self.string_length))
        boolean_value = random.choice([True, False])
        return Data(integer_value, double_value, string_value, boolean_value)

if __name__ == "__main__":
    generator = RandomDataGenerator()

    # 获取生成器对象
    data_generator = generator.generate_data

    # 生成并打印 10 个随机数据结构
    for _ in range(10):
        data = data_generator()
        print(data)

    # 打印统计信息
    stats = RandomDataGenerator.stats.get_stats()
    print(f"Method call count: {stats['call_count']}")
    print(f"Total execution time: {stats['total_time']} seconds")
    print(f"Average execution time: {stats['average_time']} seconds")
