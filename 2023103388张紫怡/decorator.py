import random
import string
from functools import wraps


class decorator:
    def __init__(self, static=None):
        self._static = static if static is not None else ['SUM', 'AVG']
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)  # 传递位置参数和关键字参数
            if result is None:
                return None
            operations = self._static if isinstance(self._static, list) else [self._static]
            for operation in operations:
                if operation == "SUM":
                    self.SUM(result)
                elif operation == "AVG":
                    self.AVG(result)
            return result
        return wrapper
    def SUM(self, result):
        total_sum = 0
        for item in result:
            for i in item:
                if isinstance(i, (int, float)) and not isinstance(i,bool):
                    total_sum+=i
        print("SUM={:.2f}".format(total_sum))
    def AVG(self, result):
        total_sum = 0
        q=0
        for item in result:
            q=q+1
            for i in item:
                if isinstance(i, (int, float)) and not isinstance(i,bool):
                    total_sum+=i
        avg = total_sum / q
        print("AVG={:.2f}".format(avg))
class DataSamplingForClass:
    def __init__(self, **kwargs):
        self.num = kwargs.get('num')
        self.struct = kwargs.get('struct')
    def generate_int(self, value):
        it = iter(value['datarange'])
        return random.randint(next(it), next(it))
    def generate_float(self, value):
        it = iter(value['datarange'])
        float_value = random.uniform(next(it), next(it))
        return round(float_value, value.get('decimals', 2))
    def generate_str(self, value):
        return ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['strlen']))
    def generate_bool(self, value):
        return [random.choice((True, False)) for _ in range(value["number"])]
    def generate_sample(self):
        result = []
        for _ in range(0,self.num):
            element = []
            for key, value in self.struct.items():
                if value['datatype'] == "int":
                    element.append(self.generate_int(value))
                elif value['datatype'] == "float":
                    element.append(self.generate_float(value))
                elif value['datatype'] == "str":
                    element.append(self.generate_str(value))
                elif value['datatype'] == "bool":
                    element.extend(self.generate_bool(value))
                else:
                    # 可以选择抛出异常、记录错误或跳过
                    continue
            result.append(element)
        return result
@decorator()
def RandomData(**kwargs):
    data=DataSamplingForClass(**kwargs).generate_sample()
    return data

if __name__ == "__main__":
    para = {'num': 3,
            'struct': {
                'int_name': {'datatype': 'int', 'datarange': [0, 10]},
                'float_name': {'datatype': 'float', 'datarange': [1.0, 5.0], 'decimals': 3},
                'str_name': {'datatype': 'str', 'datarange': string.ascii_lowercase, 'strlen': 5},
                'bool_name': {'datatype': 'bool', 'number': 3}
            }}
    data=RandomData(**para)
    for i in data:
        print(i)

