import random

class RandomDataGenerator:
    def __init__(self):
        pass

    def generate_int(self, datarange):
        return random.randint(datarange[0], datarange[1])

    def generate_float(self, datarange):
        return random.uniform(datarange[0], datarange[1])

    def generate_str(self, datarange, length):
        return ''.join(random.SystemRandom().choice(datarange) for _ in range(length))

class StructuredDataSampler(RandomDataGenerator):
    def __init__(self):
        super().__init__()

    def struct_data_sampling(self, num, struct):
        result = []
        for _ in range(num):
            element = {}
            for key, value in struct.items():
                if value['datatype'] == 'int':
                    tmp = self.generate_int(value['datarange'])
                elif value['datatype'] == 'float':
                    tmp = self.generate_float(value['datarange'])
                elif value['datatype'] == 'str':
                    tmp = self.generate_str(value['datarange'], value['len'])
                else:
                    continue
                element[key] = tmp
            result.append(element)
        return result

def show(data):
    for element in data:
        print(element)

if __name__ == '__main__':
    try:
        sampler = StructuredDataSampler()
        demo = sampler.struct_data_sampling(num=3, struct={
            '整数': {'datatype': 'int', 'datarange': [0, 500]},
            '浮点数': {'datatype': 'float', 'datarange': [0.0, 1000.0]},
            '字符串': {'datatype': 'str', 'datarange': 'abc', 'len': 10}
        })
        show(demo)
    except (TypeError, KeyError) as e:
        print(f"输入正确的参数，格式为:num=整数, struct={{'data1':{{'datatype':'int or float', 'datarange':[0,100]}}}}: {e}")