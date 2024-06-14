import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def example_function(n):
    """一个示例函数，用于计算前n个数的平方和"""
    return sum(i * i for i in range(n))

result = example_function(1000000)
print(result)
