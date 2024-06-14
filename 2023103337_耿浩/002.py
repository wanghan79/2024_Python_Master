import random

class StructDataSampler:
    def __init__(self, num=0, struct=None):
        self.num = num
        self.struct = struct

    @staticmethod
    def generate_int(datarange):
        return random.randint(datarange[0], datarange[1])

    @staticmethod
    def generate_float(datarange):
        return random.uniform(datarange[0], datarange[1])

    @staticmethod
    def generate_str(datarange, length):
        return ''.join(random.SystemRandom().choice(datarange) for _ in range(length))

    def sample(self):
        result = []
        for _ in range(self.num):
            element = {}
            for key, value in self.struct.items():
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

# Example usage:
if __name__ == "__main__":
    try:
        sampler = StructDataSampler(num=3, struct={
            '整数': {'datatype': 'int', 'datarange': [0, 500]},
            '浮点数': {'datatype': 'float', 'datarange': [0.0, 1000.0]},
            '字符串': {'datatype': 'str', 'datarange': 'abc', 'len': 10}
        })
        sampled_data = sampler.sample()
        for data in sampled_data:
            print(data)
    except (TypeError, KeyError) as e:
        print(f"输入正确的参数，格式为:num=整数, struct={{'data1':{{'datatype':'int or float', 'datarange':[0,100]}}}}: {e}")