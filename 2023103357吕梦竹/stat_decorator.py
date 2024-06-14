from functools import wraps

def stat_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Function {func.__name__} called with args: {args}, kwargs: {kwargs}, returned: {result}')
        return result
    return wrapper

@stat_decorator
def add(a, b):
    return a + b

@stat_decorator
def multiply(a, b):
    return a * b

# 使用例子
if __name__ == "__main__":
    print(add(3, 5))
    print(multiply(4, 6))
