import random
import string
from functools import wraps


class RandomStructureGenerator:
    def __init__(self, num, struct):
        if num <= 0:
            raise ValueError('Number of samples must be greater than 0')
        if not struct:
            raise ValueError('Struct cannot be empty')

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
                    element[key] = ''.join(
                        random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
                else:
                    raise ValueError(f"Unsupported data type: {datatype}")
            result.append(element)
        return result


def dataProcess(*operations):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            results = {'data': data}
            for op in operations:
                if op == 'SUM':
                    results['sum'] = {key: sum(d[key] for d in data if isinstance(d[key], (int, float))) for key in
                                      data[0]}
                elif op == 'AVG':
                    results['avg'] = {key: sum(d[key] for d in data if isinstance(d[key], (int, float))) / len(data) for
                                      key in data[0]}
            return results

        return wrapper

    return decorator


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


@dataProcess('SUM', 'AVG')
def generateData(num, struct):
    generator = RandomStructureGenerator(num, struct)
    return generator.generate()

def run():
    print("Running test3...")
    samples = generateData(num=3, struct=struct1)
    print(samples)

samples = generateData(num=3, struct=struct1)
print(samples)
