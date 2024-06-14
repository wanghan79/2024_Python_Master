import random
from functools import wraps

def datasampling(struct, num):
    """
    根据结构描述生成随机数据

    Args:
    - struct: 包含数据类型和范围的结构描述，格式为 [(type, params), ...]
      其中 type 可以是 'int', 'float', 'str'
      params 是一个元组，根据不同的 type 包含不同的参数：
        - 对于 'int': (min_value, max_value)
        - 对于 'float': (min_value, max_value)
        - 对于 'str': (length, charset)
          length 是字符串长度，charset 是字符串字符集
    - num: 生成数据的数量

    Returns:
    - 生成的随机数据列表，每个元素为一个符合结构描述的随机数据
    """
    generated_data = []

    for _ in range(num):
        data_entry = []
        for data_type, params in struct:
            if data_type == 'int':
                min_val, max_val = params
                data_entry.append(random.randint(min_val, max_val))
            elif data_type == 'float':
                min_val, max_val = params
                data_entry.append(random.uniform(min_val, max_val))
            elif data_type == 'str':
                length, charset = params
                data_entry.append(''.join(random.choice(charset) for _ in range(length)))
            else:
                raise ValueError(f"Unsupported data type: {data_type}")

        generated_data.append(tuple(data_entry))

    return generated_data



def dataProcess(*operations):
    """
    数据处理装饰器，用于在生成数据后执行指定的数据处理操作。

    Args:
    - operations: 一个或多个数据处理操作，如 'SUM', 'AVG'

    Returns:
    - 装饰器函数
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            generated_data = func(*args, **kwargs)

            processed_results = []
            for operation in operations:
                if operation == 'SUM':
                    processed_results.append(sum(data[0] for data in generated_data))
                elif operation == 'AVG':
                    total_sum = sum(data[0] for data in generated_data)
                    avg_value = total_sum / len(generated_data)
                    processed_results.append(avg_value)
                else:
                    raise ValueError(f"Unsupported operation: {operation}")

            return generated_data, processed_results

        return wrapper
    return decorator

# 定义结构描述和数量
struct = [
    ('int', (1, 100)),      # 整数类型，范围是 1 到 100
    ('float', (0.0, 1.0)),  # 浮点数类型，范围是 0.0 到 1.0
    ('str', (5, 'abcdefghijklmnopqrstuvwxyz'))  # 字符串类型，长度为 5，字符集为小写字母
]
num_samples = 10  # 生成 10 条数据

# 数据处理装饰器，计算总和和平均值
@dataProcess('SUM', 'AVG')
def generate_and_process_data(struct, num):
    return datasampling(struct, num)

# 生成随机数据并进行处理
generated_data, processed_results = generate_and_process_data(struct, num_samples)

# 打印生成的随机数据
print("Generated Data:")
for data_entry in generated_data:
    print(data_entry)

# 打印处理结果
print("\nProcessed Results:")
for i, operation in enumerate(['SUM', 'AVG']):
    print(f"{operation}: {processed_results[i]}")
