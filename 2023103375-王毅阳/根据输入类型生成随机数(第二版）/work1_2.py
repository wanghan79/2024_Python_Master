import random

#实现函数封装
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

if __name__ == '__main__':
    data_type = input("请输入数据类型（int、float、str、list、dict、tuple）：")
    random_data = generate_data(data_type)
    print('随机生成的数据为：', random_data)

# 输出结果例：
# 请输入数据类型（int、float、str、list、dict、tuple）：int
# 随机生成的数据为： 9

# 请输入数据类型（int、float、str、list、dict、tuple）：float
# 随机生成的数据为： 421.32153146559995

# 请输入数据类型（int、float、str、list、dict、tuple）：str
# 随机生成的数据为： oyvkgtnozh

# 请输入数据类型（int、float、str、list、dict、tuple）：list
# 随机生成的数据为： [81, 37, 34, 75, 92, 29, 47, 14, 61, 92]

# 请输入数据类型（int、float、str、list、dict、tuple）：dict
# 随机生成的数据为： {'key_0': 19, 'key_1': 45, 'key_2': 90, 'key_3': 68, 'key_4': 24, 'key_5': 80, 'key_6': 83, 'key_7': 67, 'key_8': 58, 'key_9': 72}

# 请输入数据类型（int、float、str、list、dict、tuple）：tuple
# 随机生成的数据为： (12, 23, 16, 31, 68, 31, 33, 67, 77, 100)