import time

def statistics_decorator(method):
    count = 0
    total_time = 0

    def wrapper(*args, **kwargs):
        nonlocal count, total_time
        start_time = time.time()
        result = method(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        count += 1
        total_time += execution_time
        return result

    return wrapper

# Test the decorator
class TestClass:
    @statistics_decorator
    def test_method(self, x):
        time.sleep(0.1)
        return x * 2

test_instance = TestClass()
for _ in range(5):
    print(test_instance.test_method(_))