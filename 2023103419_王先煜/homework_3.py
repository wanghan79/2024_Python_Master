import time
from functools import wraps

def error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"错误发生在 {func.__name__}: {e}")
            return None
    return wrapper

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 运行用了 {end_time - start_time:.6f} 秒.")
        return result
    return wrapper

@timing_decorator
@error_handler
def potentially_faulty_function(x):
    if x < 0:
        raise ValueError("不允许为负值")
    else:
        return x * x

@timing_decorator
@error_handler
def divide_numbers(x, y):
    return x / y

print(potentially_faulty_function(2))
print(potentially_faulty_function(-1))  
print(divide_numbers(10, 2))
print(divide_numbers(10, 0))  
