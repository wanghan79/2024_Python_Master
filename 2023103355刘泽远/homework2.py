import random
import string

class Data:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Data(value={self.value})"

class RandomDataGenerator:
    def __init__(self, int_range=(0, 100), double_range=(0.0, 1.0), str_length=10, list_length=5):
        self.int_range = int_range
        self.double_range = double_range
        self.str_length = str_length
        self.list_length = list_length

    def generate_integer(self):
        return random.randint(self.int_range[0], self.int_range[1])

    def generate_float(self):
        return random.uniform(self.double_range[0], self.double_range[1])

    def generate_string(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=self.str_length))

    def generate_list(self):
        return [random.choice([self.generate_integer, self.generate_float, self.generate_string])() for _ in range(self.list_length)]

    def generate_tuple(self):
        return tuple(self.generate_list())

    def generate_dict(self):
        return {f'key_{i}': random.choice([self.generate_integer, self.generate_float, self.generate_string])() for i in range(self.list_length)}

    def generate(self, data_type):
        if data_type == 'integer':
            return Data(self.generate_integer())
        elif data_type == 'float':
            return Data(self.generate_float())
        elif data_type == 'string':
            return Data(self.generate_string())
        elif data_type == 'list':
            return Data(self.generate_list())
        elif data_type == 'tuple':
            return Data(self.generate_tuple())
        elif data_type == 'dict':
            return Data(self.generate_dict())
        else:
            raise ValueError(f"Unsupported data type: {data_type}")

if __name__ == "__main__":
    valid_data_types = ['integer', 'float', 'string', 'list', 'tuple', 'dict']
    data_types = input(f"请输入想要的数据类型（例如：integer,float,string，支持的类型：{valid_data_types}）: ").split(',')
    counts = list(map(int, input("请输入对应的数量（例如：3,5,2）: ").split(',')))

    if len(data_types) != len(counts):
        raise ValueError("数据类型的数量和对应的数量必须一致")

    for data_type in data_types:
        if data_type not in valid_data_types:
            raise ValueError(f"Unsupported data type: {data_type}. Supported data types are: {valid_data_types}")

    generator = RandomDataGenerator()

    for data_type, count in zip(data_types, counts):
        for _ in range(count):
            data = generator.generate(data_type)
            print(data)
