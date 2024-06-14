import random

def datasampling(**kwargs):
    result = []
    try:
        n = kwargs['num']
    except KeyError:
        raise ValueError("Missing parameter 'num'!")
    
    if n < 0:
        raise ValueError("Parameter 'num' must be a non-negative integer!")
    
    try:
        Item = kwargs['struct']
    except KeyError:
        raise ValueError("Missing parameter 'struct'!")
    
    if not isinstance(Item, dict):
        raise TypeError("Parameter 'struct' must be a dictionary!")
    
    for _ in range(n):
        element = {}
        for key, value in Item.items():
            if value['datatype'] == 'int':
                element[key] = random.randint(*value['datarange'])
            elif value['datatype'] == 'float':
                element[key] = random.uniform(*value['datarange'])
            elif value['datatype'] == 'str':
                element[key] = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                raise ValueError(f"Unsupported datatype '{value['datatype']}' for field '{key}'")
        
        result.append(element)

    return result


struct1 = {
    'fieldname1': {
        'datatype': 'int',
        'datarange': (1, 200)  
    },
    'fieldname2': {
        'datatype': 'str',
        'datarange': 'abcdefghijklmnopqrstuvwxyz',
        'len': 4
    },
    'fieldname3': {
        'datatype': 'float',
        'datarange': (0, 2) 
    }
}


samples1 = datasampling(num=3, struct=struct1)
print(samples1)
