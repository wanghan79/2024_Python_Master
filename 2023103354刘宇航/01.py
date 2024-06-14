import random

def datasampling_v2(num_samples, struct):
    result = []
    
    for _ in range(num_samples):
        element = {}
        for key, value in struct.items():
            datatype = value.get('datatype')
            if datatype == 'int':
                datarange = value.get('datarange')
                if datarange is None:
                    raise ValueError(f'Missing datarange for field {key}')
                element[key] = random.randint(*datarange)
            elif datatype == 'float':
                datarange = value.get('datarange')
                if datarange is None:
                    raise ValueError(f'Missing datarange for field {key}')
                element[key] = random.uniform(*datarange)
            elif datatype == 'str':
                datarange = value.get('datarange')
                length = value.get('len')
                if datarange is None or length is None:
                    raise ValueError(f'Missing datarange or length for field {key}')
                element[key] = ''.join(random.choices(datarange, k=length))
            else:
                raise ValueError(f'Unsupported datatype: {datatype} for field {key}')
        result.append(element)
    
    return result
