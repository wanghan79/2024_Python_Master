#随机结构生成函数封装
import random

def datasampling(**kwargs):
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

samples1 = datasampling(num=3, struct=struct1)
print(samples1)

