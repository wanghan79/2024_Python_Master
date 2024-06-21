import random

#实现类封装  结果例:work2_2
class RandomDataGenerator:
    def __init__(self):
        self.random = random

    def generate_int(self, low=0, high=1000):
        return self.random.randint(low, high)

    def generate_float(self, low=0.0, high=1000.0):
        return self.random.uniform(low, high)

    def generate_str(self, length=10):
        return ''.join(self.random.choices('abcdefghijklmnopqrstuvwxyz', k=length))

    def generate_list(self, length=10, low=0, high=100):
        return [self.random.randint(low, high) for _ in range(length)]

    def generate_dict(self, length=10, low=0, high=100):
        return {f'key_{i}': self.random.randint(low, high) for i in range(length)}

    def generate_tuple(self, length=10, low=0, high=100):
        return tuple(self.random.randint(low, high) for _ in range(length))

    def generate_data(self, data_type, **kwargs):
        if data_type == 'int':
            return self.generate_int(**kwargs)
        elif data_type == 'float':
            return self.generate_float(**kwargs)
        elif data_type == 'str':
            return self.generate_str(**kwargs)
        elif data_type == 'list':
            return self.generate_list(**kwargs)
        elif data_type == 'dict':
            return self.generate_dict(**kwargs)
        elif data_type == 'tuple':
            return self.generate_tuple(**kwargs)
        else:
            return None
if __name__ == '__main__':
    generator = RandomDataGenerator()
    data_type = input("请输入数据类型（int、float、str、list、dict）：")
    random_data = generator.generate_data(data_type)
    print('随机生成的数据为：', random_data)
