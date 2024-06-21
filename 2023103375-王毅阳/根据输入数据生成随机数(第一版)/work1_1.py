import random

#实现函数封装
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
        return tuple(random.randint(0, 1000) for _ in range(len(instance)))
    else:
        return None


if __name__ == '__main__':
    data = eval(input("请输入数据："))
    random_data = generate_random_value(data)
    print('随机生成的数据为：', random_data)

# 输出结果例：

# 请输入数据：[1,2,3,4]
# 随机生成的数据为： [250, 57, 471, 804]

# 请输入数据：1
# 随机生成的数据为： 901

# 请输入数据：1.0
# 随机生成的数据为： 633.3628481796286

# 请输入数据："example"
# 随机生成的数据为： mgdzwnismg

# 请输入数据：{"key1": 1, "key2": 2}
# 随机生成的数据为： {'key1': 924, 'key2': 906}

# 请输入数据：(1, 2, 3)
# 随机生成的数据为： (805, 357, 528)