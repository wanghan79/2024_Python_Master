import random
import string

def generate_int(datarange):
    return random.randint(*datarange)

def generate_float(datarange):
    return random.uniform(*datarange)
def generate_str(characters, length):
    return ''.join(random.choice(characters) for _ in range(length))

def structured_data_sampler(num, struct):
    def decorator(func):
        def wrapper():
            result = []
            for _ in range(num):
                element = {key: generate_data(value) for key, value in struct.items()}
                result.append(element)
            func(result)
        return wrapper
    return decorator

def generate_data(data_spec):
    if data_spec['datatype'] == 'int':
        return generate_int(data_spec['datarange'])
    elif data_spec['datatype'] == 'float':
        return generate_float(data_spec['datarange'])
    elif data_spec['datatype'] == 'str':
        return generate_str(data_spec['datarange'], data_spec['len'])

def show(data):
    for element in data:
        print(element)

@structured_data_sampler(num=3, struct={
    '整数': {'datatype': 'int', 'datarange': [0, 500]},
    '浮点数': {'datatype': 'float', 'datarange': [0.0, 1000.0]},
    '字符串': {'datatype': 'str', 'datarange': string.ascii_lowercase, 'len': 10}
})
def process_data(data):
    show(data)

if __name__ == '__main__':
    try:
        process_data()
    except Exception as e:
        print(f"发生错误: {e}")
