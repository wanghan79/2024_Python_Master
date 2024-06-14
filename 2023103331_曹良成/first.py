import random
import string


def dataSampling(**kwargs):
    result = []
    for key, value in kwargs.items():
        if key == 'int':
            result.append(random.randint(0, value))
        elif key == 'float':
            result.append(random.uniform(0, value))
        elif key == 'str':
            length = value
            result.append(''.join(random.choices(string.ascii_letters + string.digits, k=length)))
    return result
