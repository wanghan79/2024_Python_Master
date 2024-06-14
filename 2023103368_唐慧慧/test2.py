import random
import string
from functools import wraps

def datasampling(**kwargs):
    """
    :param kwargs: dict containing num and struct
    :return: list of generated data
    """
    result = []
    n = kwargs.get('num', -1)
    if n == -1:
        raise Exception('Missing Parameter num!')
    Item = kwargs.get('struct', None)
    if Item is None:
        raise Exception('Missing Parameter struct!')
    for _ in range(n):
        element = []
        for key, value in Item.items():
            if value['datatype'] == 'int':
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif value['datatype'] == 'float':
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif value['datatype'] == 'str':
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element.append(tmp)
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
                    results['sum'] = [sum(d) if isinstance(d[0], (int, float)) else None for d in zip(*data)]
                elif op == 'AVG':
                    results['avg'] = [sum(d) / len(d) if isinstance(d[0], (int, float)) else None for d in zip(*data)]
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
        'datarange': 'abcdefghijklmnopqrstuvwxyz',
        'len': 4
    },
    'fieldname3': {
        'datatype': 'float',
        'datarange': [0, 2]
    }
}

@dataProcess('SUM', 'AVG')
def generateData(num, struct):
    return datasampling(num=num, struct=struct)

def run():
    print("Running test2...")
    samples = generateData(num=3, struct=struct1)
    print(samples)

samples = generateData(num=3, struct=struct1)
print(samples)
