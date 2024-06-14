'''
第三次作业：完成通过修饰器实现
'''
import random
from functools import wraps

def validate_params(required_params):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 检查必需的参数是否存在
            for param in required_params:
                if param not in kwargs:
                    raise ValueError(f"Missing required parameter: {param}")

            rand_type = kwargs['type']
            rand_range = kwargs['range']
            rand_size = kwargs['size']

            # 检查 'range' 参数是否有效
            if not (isinstance(rand_range, (list, tuple)) and len(rand_range) == 2 and rand_range[0] <= rand_range[1]):
                raise ValueError("Invalid range parameter")

            # 检查 'size' 参数是否有效
            if not (isinstance(rand_size, int) and rand_size > 0):
                raise ValueError("Invalid size parameter")

            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_params(['type', 'range', 'size'])
def generate_random_numbers(**params):
    rand_type = params['type']
    rand_range = params['range']
    rand_size = params['size']

    # 生成随机数列表
    if rand_type == 'int':
        rand_nums = [random.randint(rand_range[0], rand_range[1]) for _ in range(rand_size)]
    elif rand_type == 'float':
        rand_nums = [random.uniform(rand_range[0], rand_range[1]) for _ in range(rand_size)]
    else:
        raise ValueError("Invalid type parameter")

    return rand_nums

# 示例参数
params1 = {'type': 'int', 'range': (1, 100), 'size': 5}
params2 = {'type': 'float', 'range': (0.0, 1.0), 'size': 3}

# 生成随机数
random_integers = generate_random_numbers(**params1)
random_floats = generate_random_numbers(**params2)

# 输出结果
print("随机整数:", random_integers)
print("随机浮点数:", random_floats)
