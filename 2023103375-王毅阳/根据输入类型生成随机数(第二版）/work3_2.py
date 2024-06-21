import random

# 生成随机数的函数
def generate_data(data_type):
    if data_type == 'int':
        return random.randint(0, 1000)
    elif data_type == 'float':
        return random.uniform(0.0, 1000.0)
    elif data_type == 'str':
        return ''.join(random.choices('abcdefghigklmnopqrstuvwxyz', k=10))
    elif data_type == 'list':
        return [random.randint(0, 100) for _ in range(10)]
    elif data_type == 'dict':
        return {f'key_{i}': random.randint(0, 100) for i in range(10)}
    elif data_type == 'tuple':
        return tuple(random.randint(0, 100) for _ in range(10))
    else:
        return None

# 修饰器：根据示例数据类型生成随机数据
def random_value_decorator(func):
    def wrapper(*args, **kwargs):
        instance = args[0]  # 第一个参数作为示例数据类型
        random_value = generate_data(instance)
        return func(random_value, *args[1:], **kwargs)
    return wrapper

# 示例函数：接收随机值并返回
@random_value_decorator
def instance_function(value):
    return value

# 示例使用
if __name__ == '__main__':
    int_count = int(input("输入想生成的整数随机数数量："))
    float_count = int(input("输入想生成的浮点数随机数数量："))
    string_count = int(input("输入想生成的字符串随机数数量："))
    list_count = int(input("输入想生成的列表随机数数量："))
    dict_count = int(input("输入想生成的字典随机数数量："))
    tuple_count = int(input("输入想生成的元组随机数数量："))
    for _ in range(int_count):
        instance = 'int'
        print(instance_function(instance))

    for _ in range(float_count):
        instance = 'float'
        print(instance_function(instance))

    for _ in range(string_count):
        instance = 'str'
        print(instance_function(instance))

    for _ in range(list_count):
        instance = 'list'
        print(instance_function(instance))

    for _ in range(dict_count):
        instance = 'dict'
        print(instance_function(instance))

    for _ in range(tuple_count):
        instance = 'tuple'
        print(instance_function(instance))

# 结果：
# 输入想生成的整数随机数数量：3
# 输入想生成的浮点数随机数数量：5
# 输入想生成的字符串随机数数量：4
# 输入想生成的列表随机数数量：6
# 输入想生成的字典随机数数量：5
# 输入想生成的元组随机数数量：3
# 292
# 1
# 286
# 22.93095189344918
# 972.3588612947865
# 101.7872126525341
# 377.5271291045498
# 793.5871295420563
# btgoefmgip
# dqrykgzlqh
# raurxrsmhw
# yvptinoggn
# [44, 33, 26, 73, 20, 57, 16, 7, 54, 57]
# [79, 8, 17, 6, 68, 99, 56, 56, 32, 91]
# [58, 70, 12, 75, 58, 45, 37, 20, 77, 26]
# [62, 100, 91, 71, 25, 67, 26, 68, 76, 91]
# [6, 11, 63, 15, 10, 40, 55, 80, 93, 83]
# [65, 98, 68, 16, 80, 95, 18, 88, 4, 42]
# {'key_0': 3, 'key_1': 31, 'key_2': 35, 'key_3': 93, 'key_4': 9, 'key_5': 92, 'key_6': 24, 'key_7': 0, 'key_8': 68, 'key_9': 52}
# {'key_0': 74, 'key_1': 3, 'key_2': 65, 'key_3': 47, 'key_4': 60, 'key_5': 91, 'key_6': 22, 'key_7': 49, 'key_8': 97, 'key_9': 66}
# {'key_0': 56, 'key_1': 70, 'key_2': 91, 'key_3': 34, 'key_4': 51, 'key_5': 3, 'key_6': 36, 'key_7': 30, 'key_8': 38, 'key_9': 52}
# {'key_0': 79, 'key_1': 36, 'key_2': 22, 'key_3': 10, 'key_4': 37, 'key_5': 14, 'key_6': 15, 'key_7': 49, 'key_8': 80, 'key_9': 22}
# {'key_0': 64, 'key_1': 81, 'key_2': 86, 'key_3': 9, 'key_4': 98, 'key_5': 59, 'key_6': 47, 'key_7': 10, 'key_8': 3, 'key_9': 66}
# (29, 36, 29, 41, 15, 17, 51, 7, 38, 80)
# (22, 27, 43, 55, 51, 41, 21, 32, 25, 75)
# (63, 34, 58, 67, 17, 71, 99, 37, 11, 7)
