import random

def struct_datasampling(**kwargs):
    num_samples = kwargs['num']
    data_structure = kwargs['struct']
    results = []

    for _ in range(num_samples):
        element = []
        for key, specs in data_structure.items():
            datatype = specs['datatype']
            datarange = specs['datarange']
            if datatype == 'int':
                temp = random.randint(*datarange)
            elif datatype == 'float':
                temp = random.uniform(*datarange)
            elif datatype == 'str':
                temp = ''.join(random.choice(specs['datarange']) for _ in range(specs['strlen']))
            else:
                continue
            element.append(temp)
        results.append(element)

    return results

example = {
    "num": 10,
    "struct": {
        "a": {
            "datatype": "int",
            "datarange": (0, 100)
        },
        "b": {
            "datatype": "float",
            "datarange": (-199, 200)
        },
        "d": {
            "datatype": "str",
            "datarange": "qjjdiehaincbcuieudhdh",
            "strlen": 8
        }
    }
}

print(struct_datasampling(**example))
