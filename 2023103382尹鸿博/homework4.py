import random
import string
from functools import wraps

# 统计装饰器
def stats_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        result = func(*args, **kwargs)
        print(f"{func.__name__} called {wrapper.call_count} times")
        return result
    wrapper.call_count = 0
    return wrapper

@stats_decorator
def generate_integer(int_range):
    while True:
        yield random.randint(int_range[0], int_range[1])

@stats_decorator
def generate_float(double_range):
    while True:
        yield random.uniform(double_range[0], double_range[1])

@stats_decorator
def generate_string(str_length):
    while True:
        yield ''.join(random.choices(string.ascii_letters + string.digits, k=str_length))

@stats_decorator
def generate_list(int_range, double_range, str_length, list_length):
    while True:
        yield [random.choice([
            lambda: next(generate_integer(int_range)),
            lambda: next(generate_float(double_range)),
            lambda: next(generate_string(str_length))
        ])() for _ in range(list_length)]

@stats_decorator
def generate_tuple(int_range, double_range, str_length, list_length):
    while True:
        yield tuple(next(generate_list(int_range, double_range, str_length, list_length)))

@stats_decorator
def generate_dict(int_range, double_range, str_length, list_length):
    while True:
        yield {f'key_{i}': random.choice([
            lambda: next(generate_integer(int_range)),
            lambda: next(generate_float(double_range)),
            lambda: next(generate_string(str_length))
        ])() for i in range(list_length)}

def generate_data(data_type, int_range=(0, 100), double_range=(0.0, 1.0), str_length=10, list_length=5):
    if data_type == 'integer':
        return generate_integer(int_range)
    elif data_type == 'float':
        return generate_float(double_range)
    elif data_type == 'string':
        return generate_string(str_length)
    elif data_type == 'list':
        return generate_list(int_range, double_range, str_length, list_length)
    elif data_type == 'tuple':
        return generate_tuple(int_range, double_range, str_length, list_length)
    elif data_type == 'dict':
        return generate_dict(int_range, double_range, str_length, list_length)
    else:
        raise ValueError(f"Unsupported data type: {data_type}")

if __name__ == "__main__":
    data_types = input("请输入想要的数据类型（例如：integer,float,string）: ").split(',')
    counts = list(map(int, input("请输入对应的数量（例如：3,5,2）: ").split(',')))

    if len(data_types) != len(counts):
        raise ValueError("数据类型的数量和对应的数量必须一致")

    int_range = (0, 100)
    double_range = (0.0, 1.0)
    str_length = 10
    list_length = 5

    for data_type, count in zip(data_types, counts):
        generator = generate_data(data_type, int_range, double_range, str_length, list_length)
        for _ in range(count):
            print(next(generator))
