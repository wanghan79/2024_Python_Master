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

# 修饰器函数
def structured_data_sampler(num=0, struct={}):
    def decorator(func):
        def wrapper():
            result = []
            for _ in range(num):
                element = {}
                for key, value in struct.items():
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
            func(result)
        return wrapper
    return decorator

def show(data):
    for element in data:
        print(element)

# 使用修饰器生成数据
@structured_data_sampler(num=3, struct={
    '整数': {'datatype': 'int', 'datarange': [0, 500]},
    '浮点数': {'datatype': 'float', 'datarange': [0.0, 1000.0]},
    '字符串': {'datatype': 'str', 'datarange': 'abc', 'len': 10}
})
def generate_and_show(data):
    show(data)

# 主函数调用
if __name__ == '__main__':
    try:
        generate_and_show()
    except (TypeError, KeyError) as e:
        print(f"输入正确的参数，格式为:num=整数, struct={{'data1':{{'datatype':'int or float', 'datarange':[0,100]}}}}: {e}")