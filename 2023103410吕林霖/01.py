import random
from functools import wraps
import time

# 定义修饰器,用于记录函数运行时间
def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end-start:.6f} seconds to run.")
        return result
    return wrapper

# 生成器函数,生成随机整数
def random_integers(low, high, count):
    for _ in range(count):
        yield random.randint(low, high)

# 生成器函数,生成随机浮点数
def random_floats(low, high, count, precision=2):
    for _ in range(count):
        yield round(random.uniform(low, high), precision)

# 主函数,生成随机结构
@timing
def generate_random_struct(struct_type, *args):
    if struct_type == 'int':
        return list(random_integers(*args))
    elif struct_type == 'float':
        return list(random_floats(*args))
    else:
        raise ValueError("Invalid struct type. Use 'int' or 'float'.")

# 使用示例
int_list = generate_random_struct('int', 1, 100, 10)
print(int_list)

float_list = generate_random_struct('float', 0, 1, 5, 3)
print(float_list)