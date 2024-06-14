import random

# 生成随机整数
def generate_int(datarange):
    return random.randint(datarange[0], datarange[1])

# 生成随机浮点数
def generate_float(datarange):
    return random.uniform(datarange[0], datarange[1])

# 生成随机字符串
def generate_str(datarange, length):
    return ''.join(random.SystemRandom().choice(datarange) for _ in range(length))

# 结构化数据采样函数
def structDataSampling(**kwargs):
    result = []
    for _ in range(kwargs.get('num', 0)):
        element = {}
        for key, value in kwargs.get('struct', {}).items():
            if value['datatype'] == 'int':
                tmp = generate_int(value['datarange'])
            elif value['datatype'] == 'float':
                tmp = generate_float(value['datarange'])
            elif value['datatype'] == 'str':
                tmp = generate_str(value['datarange'], value['len'])
            else:
                continue
            element[key] = tmp
        result.append(element)
    return result

# 显示数据
def show(data):
    for element in data:
        print(element)

# 主函数
if __name__ == '__main__':
    try:
        demo = structDataSampling(num=3, struct={
            '整数': {'datatype': 'int', 'datarange': [0, 500]},
            '浮点数': {'datatype': 'float', 'datarange': [0.0, 1000.0]},
            '字符串': {'datatype': 'str', 'datarange': 'abc', 'len': 10}
        })
        show(demo)
    except (TypeError, KeyError) as e:
        print(f"输入正确的参数，格式为:num=整数, struct={{'data1':{{'datatype':'int or float', 'datarange':[0,100]}}}}: {e}")