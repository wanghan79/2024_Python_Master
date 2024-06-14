import random

def addLogging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'{func.__name__} is running at level {level}')
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

class RandomDataStatistics:
    def __init__(self, count=10):
        self.random_numbers = []
        self.count = count

    @staticmethod
    @addLogging('high')
    def sum_values(*args):
        total_sum = sum(args)  # Calculate sum
        print(f'The sum is {total_sum}')
        return total_sum

    @staticmethod
    @addLogging('low')
    def mean_values(*args):
        total_sum = sum(args)  # Calculate sum
        avg = total_sum / len(args)
        print(f'The average is {avg}')
        return avg

# Usage example
if __name__ == "__main__":
    rds = RandomDataStatistics()

    rds.sum_values(3, 3, 8)  # Calculate sum
    rds.mean_values(3, 3, 9)  # Calculate mean
