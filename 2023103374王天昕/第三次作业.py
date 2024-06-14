import random

def addLogging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'{func.__name__} is running at level {level}')
            total_sum = sum(args)  # 计算总和
            print(f'The sum is {total_sum}')
            return func(*args, **kwargs)
        return wrapper
    return decorator

class RandomDataStatistics:
    def __init__(self, count=10):
        self.random_numbers = []
        self.count = count

    @staticmethod
    @addLogging('high')
    def sum(*args):
        return sum(args)

    @staticmethod
    @addLogging('low')
    def mean(*args):
        total_sum = sum(args)
        avg = total_sum / len(args)
        print(f'The average is {avg}')
        return avg

# 使用示例
if __name__ == "__main__":
    rds = RandomDataStatistics()

    rds.sum(3, 3, 8)  # 计算总和
    rds.mean(3, 3, 9)  # 计算均值
