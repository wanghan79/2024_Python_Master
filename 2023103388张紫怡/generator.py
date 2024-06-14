import random
import string

class DataSamplingForClassForGenerator:
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
    ##素数那个
    def __iter__(self):
        for _ in range(0,self.num):
            element = []
            for key, value in self.struct.items():
                if value['datatype'] == int:
                    element.append(self.generate_int(value))
                elif value['datatype'] == float:
                    element.append(self.generate_float(value))
                elif value['datatype']== str:
                    element.append(self.generate_str(value))
                elif value['datatype'] == bool:
                    element.extend(self.generate_bool(value))
                else:
                    # 可以选择抛出异常、记录错误或跳过
                    continue
            yield element
if __name__ == "__main__":
    para = {'num': 3,
            'struct': {
                'int_name': {'datatype': int, 'datarange': [0, 10]},
                'float_name': {'datatype': float, 'datarange': [1.0, 5.0], 'decimals': 3},
                'str_name': {'datatype': str, 'datarange': string.ascii_lowercase, 'strlen': 5},
                'bool_name': {'datatype': bool, 'number': 3}
            }}
    struct_data = DataSamplingForClass(**para)
    for element in struct_data:
        print(element)
