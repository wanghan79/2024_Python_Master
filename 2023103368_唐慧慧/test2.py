import random
import string

class RandomStructureGenerator:
    def __init__(self, num, struct):
        self.num = num
        self.struct = struct

    def generate(self):
        result = []
        for _ in range(self.num):
            element = {}
            for key, value in self.struct.items():
                datatype = value['datatype']
                if datatype == 'int':
                    it = iter(value['datarange'])
                    element[key] = random.randint(next(it), next(it))
                elif datatype == 'float':
                    it = iter(value['datarange'])
                    element[key] = random.uniform(next(it), next(it))
                elif datatype == 'str':
                    element[key] = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
                else:
                    raise ValueError(f"Unsupported data type: {datatype}")
            result.append(element)
        return result

# 测试数据
struct1 = {
    'fieldname1': {
        'datatype': 'int',
        'datarange': [1, 200]
    },
    'fieldname2': {
        'datatype': 'str',
        'datarange': string.ascii_lowercase,
        'len': 4
    },
    'fieldname3': {
        'datatype': 'float',
        'datarange': [0, 2]
    }
}

def run():
    print("Running test2...")
    generator = RandomStructureGenerator(num=3, struct=struct1)
    samples = generator.generate()
    print(samples)
# 测试生成器类
generator = RandomStructureGenerator(num=3, struct=struct1)
samples = generator.generate()
print(samples)
