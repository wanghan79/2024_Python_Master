import random
from functools import wraps
import time

from statistics import mean, fsum


def add_logging(dec_para):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'{func.__name__} is running')
            total_sum = sum(args)
            print(f'The sum is {total_sum}')
            return func(*args, **kwargs)
        return wrapper
    return decorator

class RandomDataStatistics:
    def __init__(self, count=10):
        self.random_numbers = [random.randint(1, 100) for _ in range(count)]
        self.count = count

    @add_logging('a level')
    def calculate_sum(self, *args):
        return fsum(args)

    @add_logging('a level')
    def calculate_mean(self, *args):
        if args:
            avg = mean(args)
            print(f'The average is {avg}')
            return avg
        else:
            print('No numbers to calculate mean')
            return 0

# 使用示例
rds = RandomDataStatistics()

# 计算总和
result_sum = rds.calculate_sum(3, 3, 8)
print(f'Resulting sum: {result_sum}')

# 计算均值
result_mean = rds.calculate_mean(3, 3, 9)
print(f'Resulting mean: {result_mean}')
