
import random
from functools import wraps

# 修饰器：用于统计每种数据类型生成的次数
def count_calls(func):
    counts = {}

    @wraps(func)
    def wrapper(date_type):
        if date_type not in counts:
            counts[date_type] = 0
        counts[date_type] += 1
        return func(date_type)

    wrapper.call_counts = counts
    return wrapper

# 随机数结构生成函数封装
@count_calls
def generate_date(date_type):
    match date_type:
        case 'int':
            return random.randint(0, 10)
        case 'float':
            return random.uniform(0.0, 100.0)
        case 'str':
            return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
        case 'list':
            return [random.randint(0, 100) for _ in range(5)]
        case 'dict':
            return {f'key_{i}': random.randint(0, 100) for i in range(5)}
        case _:
            return None

if __name__ == "__main__":
    # 一次性输入多种类型
    input_types = ['int', 'float', 'str', 'list', 'dict']
    input_results = {}

    for date_type in input_types:
        random_date = generate_date(date_type)
        input_results[date_type] = random_date

    # 一次性输出随机生成的数据
    print("一次性输出随机生成的数据：")
    for date_type, random_date in input_results.items():
        print(f"{date_type}: {random_date}")

    # 输出各种类型数据生成的次数
    print("\n生成次数统计：")
    for key, value in generate_date.call_counts.items():
        print(f"{key}: {value} 次")
