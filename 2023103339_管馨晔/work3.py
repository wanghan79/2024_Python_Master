import random
import string

def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        result = func(*args, **kwargs)
        print(f"{func.__name__} called {wrapper.calls} times")
        return result
    wrapper.calls = 0
    return wrapper

class RandGenStats:
    def __init__(self):
        pass

    @count_calls
    def rand_val(self):
        return random.choice([
            random.randint(1, 100),
            random.uniform(1.0, 100.0),
            ''.join(random.choices(string.ascii_letters + string.digits, k=5)),
            None,
            True,
            False
        ])

    @count_calls
    def rand_struct(self, struct):
        if isinstance(struct, list):
            return [self.rand_struct(item) for item in struct]
        elif isinstance(struct, tuple):
            return tuple(self.rand_struct(item) for item in struct)
        elif isinstance(struct, dict):
            return {key: self.rand_struct(value) for key, value in struct.items()}
        else:
            return self.rand_val()

# 示例
gen_stats = RandGenStats()
input_struct = [1, "a", {"key": (2, 3)}, [4, 5]]
random_struct_stats = gen_stats.rand_struct(input_struct)
print(random_struct_stats)
