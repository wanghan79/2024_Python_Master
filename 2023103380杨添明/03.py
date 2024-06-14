
class StatisticDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        print(f"Function '{self.func.__name__}' was called with args: {args}, kwargs: {kwargs}")
        return result

# Usage example

@StatisticDecorator
def multiply(a, b):
    return a * b

@StatisticDecorator
def divide(a, b):
    return a / b

# Example usage
result1 = multiply(5, 3)
result2 = divide(10, 2)
