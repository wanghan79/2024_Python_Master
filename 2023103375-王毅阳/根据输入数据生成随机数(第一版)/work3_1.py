import random

# 生成随机数据的函数
def generate_random_value(instance):
    if isinstance(instance, int):
        return random.randint(0, 1000)
    elif isinstance(instance, float):
        return random.uniform(0.0, 1000.0)
    elif isinstance(instance, str):
        return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))
    elif isinstance(instance, list):
        length = len(instance)
        return [random.randint(0, 1000) for _ in range(length)]
    elif isinstance(instance, dict):
        keys = list(instance.keys())
        return {key: random.randint(0, 1000) for key in keys}
    elif isinstance(instance, tuple):
        return tuple(random.randint(0, 100) for _ in range(10))
    else:
        return None

# 修饰器：根据示例数据类型生成随机数据
def random_value_decorator(func):
    def wrapper(*args, **kwargs):
        instance = args[0]  # 第一个参数作为示例数据类型
        random_value = generate_random_value(instance)
        return func(random_value, *args[1:], **kwargs)
    return wrapper

# 示例函数：接收随机值并返回
@random_value_decorator
def instance_function(value):
    return value

# 统计并打印每种输入类型的个数及生成的随机数
def print_statistics(test_instance):
    type_counts = {
        'list': 0,
        'float': 0,
        'str': 0,
        'dict': 0,
        'tuple': 0,
        'int': 0,
        'other': 0
    }

    for instance in test_instance:
        if isinstance(instance, list):
            type_counts['list'] += 1
        elif isinstance(instance, float):
            type_counts['float'] += 1
        elif isinstance(instance, str):
            type_counts['str'] += 1
        elif isinstance(instance, dict):
            type_counts['dict'] += 1
        elif isinstance(instance, tuple):
            type_counts['tuple'] += 1
        elif isinstance(instance, int):
            type_counts['int'] += 1
        else:
            type_counts['other'] += 1

    print("输入类型统计：")
    for type_name, count in type_counts.items():
        if count > 0:
            print(f"{type_name}: {count}")

    print("\n--------------------------------------------\n")
    return type_counts

# 主程序
if __name__ == '__main__':
    # 生成大量数据
    test_instance = [
        ["test", "hello"],
        {"key1": 1, "key2": 2},
        (1, 2, 3),
        100,
        3.14,
        "example"
    ] * 500

    # 打印每种类型的个数
    type_counts = print_statistics(test_instance)

    # 调用装饰后的函数生成随机值并打印
    for instance in test_instance:
        print(instance_function(instance))

# 结果：

# 输入类型统计：
# list: 500
# float: 500
# str: 500
# dict: 500
# tuple: 500
# int: 500
#
# --------------------------------------------
#
# [708, 374]
# {'key1': 445, 'key2': 581}
# (95, 72, 12, 84, 26, 55, 46, 30, 83, 92)
# 715
# 151.36785432373912
# rtkmfnjlwl
#
# [501, 99]
# {'key1': 663, 'key2': 602}
# (37, 61, 82, 96, 31, 95, 41, 33, 39, 84)
# 749
# 198.05533045277346
# kviurdihmq

# ...（一共500个组，省略其余498个组）