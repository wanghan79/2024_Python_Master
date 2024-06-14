import time
from functools import wraps


def stats_decorator(func):
    # 装饰器，用于计算调用次数并记录函数的执行时间。
    call_count = 0
    total_time = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal call_count, total_time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        call_count += 1
        total_time += (end_time - start_time)
        print(f"Function {func.__name__} called {call_count} times. Total execution time: {total_time:.4f} seconds.")
        return result

    return wrapper


# Example usage
@stats_decorator
def example_function(x, y):
    # 示例函数
    time.sleep(0.1)  # Simulate some processing time
    return x + y


# Test the decorated function
example_function(3, 4)
example_function(5, 6)
