import random
import string

def structDataSampling(num, **kwargs):
    result = []
    for _ in range(num):
        element = []
        for key, value in kwargs.items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.choice(value['datarange']) for _ in range(value['len']))
            element.append(tmp)
        result.append(element)
    return result

def dataSampling():
    struct = {
        "num": 3,
        "int": {"datarange": [1, 100]},
        "float": {"datarange": [1.0, 100.0]},
        "str": {"datarange": string.ascii_letters, "len": 5}
    }
    samples = structDataSampling(**struct)
    for sample in samples:
        print(sample)

if __name__ == '__main__':
    dataSampling()
