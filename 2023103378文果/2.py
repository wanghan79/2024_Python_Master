import random

def dataProcess(*args):
    # use data_args variable to store args
    data_args = args
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            result = {'origin_data': data}
            for opt in data_args:
                if opt == 'AVG':
                    total_sum = sum(sum(row) for row in data)
                    num_elements = len(data) * len(data[0])
                    result['AVG'] = total_sum / num_elements
                if opt == 'SUM':
                    total_sum = sum(sum(row) for row in data)
                    result['SUM'] = total_sum
            return result
        return wrapper
    return decorator

@dataProcess('SUM', 'AVG')
def datasampling(**kwargs):
    result = []
    n = kwargs.get('num')
    if n is None:
        raise ValueError('Missing parameter: num')
    
    item_structure = kwargs.get('struct')
    if item_structure is None:
        raise ValueError('Missing parameter: struct')
    
    for _ in range(n):
        element = []
        for key, value in item_structure.items():
            datatype = value.get('datatype')
            if datatype == 'int':
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif datatype == 'float':
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif datatype == 'str':
                tmp = ''.join(random.choices(value['datarange'], k=value['len']))
            else:
                raise ValueError(f"Unsupported datatype: {datatype}")
            element.append(tmp)
        result.append(element)

    return result

structure = {
    '1': {'datatype': 'float', 'datarange': [18, 65]},
    '2': {'datatype': 'float', 'datarange': [18, 65]},
}

f = datasampling(num=2, struct=structure)
print(f)

