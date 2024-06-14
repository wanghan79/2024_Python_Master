import random
import string

class RandomDataGenerator:
    def __init__(self, *args):
        self.data_args = args

    def data_process(self, func):
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            result = {}
            result['origin_data'] = data
            for opt in self.data_args:
                if opt == 'AVG':
                    s = sum(sum(_) for _ in data)
                    result['AVG'] = s / (len(data) * len(data[0]))
                if opt == 'SUM':
                    s = sum(sum(_) for _ in data)
                    result['SUM'] = s
            return result
        return wrapper

    @staticmethod
    def generate_random_value(value_template):
        """Generate a random value based on the type and range specified in value_template."""
        if value_template['datatype'] == 'int':
            return random.randint(*value_template['datarange'])
        elif value_template['datatype'] == 'float':
            return round(random.uniform(*value_template['datarange']), 2)
        elif value_template['datatype'] == 'str':
            return ''.join(random.choice(string.ascii_lowercase) for _ in range(value_template['len']))
        else:
            return None

    def data_sampling(self, **kwargs):
        @self.data_process
        def sampling():
            result = []
            n = kwargs.get('num', -1)
            if n == -1:
                raise Exception('缺失参数num!')
            item_structure = kwargs.get('struct', None)
            if item_structure is None:
                raise Exception('缺失参数struct!')
            for _ in range(n):
                element = []
                for key, value in item_structure.items():
                    element.append(self.generate_random_value(value))
                result.append(element)
            return result
        
        return sampling()

# 定义数据结构模板
structure = {
    '1': {'datatype': 'float', 'datarange': [18, 65]},
    '2': {'datatype': 'float', 'datarange': [18, 65]},
}

# 创建一个随机数据生成器实例
generator = RandomDataGenerator('SUM', 'AVG')

# 生成随机数据并处理
result = generator.data_sampling(num=2, struct=structure)
print(result)