import random
import string

# 生成随机整数
def generate_int(datarange):
    return random.randint(datarange[0], datarange[1])

# 生成随机浮点数
def generate_float(datarange):
    return random.uniform(datarange[0], datarange[1])

# 生成随机字符串
def generate_str(datarange, length):
    return ''.join(random.choice(datarange) for _ in range(length))

# 生成器生成随机结构
def struct_data_generator(num, struct_dict):
    for _ in range(num):
        data_sample = {}
        for key, value in struct_dict.items():
            if value['datatype'] == 'int':
                data_sample[key] = generate_int(value['datarange'])
            elif value['datatype'] == 'float':
                data_sample[key] = generate_float(value['datarange'])
            elif value['datatype'] == 'str':
                data_sample[key] = generate_str(value['datarange'], value['len'])
        yield data_sample

# 显示数据
def show(data_generator):
    for element in data_generator:
        print(element)

# 主函数
if __name__ == '__main__':
    try:
        # 定义结构化数据生成参数
        struct_dict = {
            '整数': {'datatype': 'int', 'datarange': [0, 500]},
            '浮点数': {'datatype': 'float', 'datarange': [0.0, 1000.0]},
            '字符串': {'datatype': 'str', 'datarange': string.ascii_letters, 'len': 10}
        }
        num = 3
