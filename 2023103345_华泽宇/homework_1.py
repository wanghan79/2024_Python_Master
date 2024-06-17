import random

def data_sampling(num, struct):
  
    samples = []  # 存储生成的数据
    for _ in range(num):
        sample = {}  # 每个样本用一个字典表示
        for field, config in struct.items():
            
            datatype = config.get('datatype')
            if datatype == 'int':
                datarange = config.get('datarange')
                sample[field] = random.randint(datarange[0], datarange[1])
            elif datatype == 'float':
                datarange = config.get('datarange')
                sample[field] = random.uniform(datarange[0], datarange[1])
            elif datatype == 'str':
                datarange = config.get('datarange')
                length = config.get('len')
                sample[field] = ''.join(random.choice(datarange) for _ in range(length))
        samples.append(sample)

    return samples

# 示例
structure = {
    'field1': {
        'datatype': 'int',
        'datarange': [1, 200]
    },
    'field2': {
        'datatype': 'str',
        'datarange': 'abcdefghijklmnopqrstuvwxyz',
        'len': 4
    },
    'field3': {
        'datatype': 'float',
        'datarange': [0, 2]
    }
}

# 生成3个具有指定结构的样本
samples = data_sampling(num=3, struct=structure)
print(samples)