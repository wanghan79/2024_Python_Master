import random

class RandomStructureGenerator:
    def __init__(self, num_samples, data_structure):
        self.num_samples = num_samples
        self.data_structure = data_structure

    def __iter__(self):
        return self

    def __next__(self):
        if self.num_samples > 0:
            self.num_samples -= 1
            return self.generate_sample(self.data_structure)
        else:
            raise StopIteration

    def generate_sample(self, data_structure):
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
        return element

data_structure = {
    "int": {
        "datatype": "int",
        "datarange": (0, 100)
    },
    "float": {
        "datatype": "float",
        "datarange": (-100, 100)
    },
    "str": {
        "datatype": "str",
        "datarange": "abcdefghijklmnopqrstuvwxyz",
        "strlen": 5
    }
}

generator = RandomStructureGenerator(10, data_structure)

for sample in generator:
    print(sample)
