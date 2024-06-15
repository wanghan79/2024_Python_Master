import random

class StructuredDataGenerator:
    def __init__(self):
        pass

    def generate_data(self, num, structure):
        results = []
        for _ in range(num):
            element = []
            for key, specs in structure.items():
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

# 示例使用
if __name__ == "__main__":
    generator = StructuredDataGenerator()

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

    results = generator.generate_data(num=example['num'], structure=example['struct'])
    print(results)
