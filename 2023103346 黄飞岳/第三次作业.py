from functools import wraps

def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, 'call_count'):
            wrapper.call_count = 0
        wrapper.call_count += 1
        print(f"{func.__name__} has been called {wrapper.call_count} times")
        return func(*args, **kwargs)
    return wrapper


@count_calls
def generate_random_structure(structure: Any) -> Any:
    pass

# 测试
if __name__ == "__main__":
    for _ in range(5):
        generate_random_structure({})