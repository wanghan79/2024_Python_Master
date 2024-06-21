import random

#实现类封装  结果例:work2_1
class RandomDataGenerator:
    def __init__(self):
        self.random = random

    def generate_int(self, low=0, high=1000):
        return self.random.randint(low, high)

    def generate_float(self, low=0.0, high=1000.0):
        return self.random.uniform(low, high)

    def generate_str(self, length=10):
        return ''.join(self.random.choices('abcdefghijklmnopqrstuvwxyz', k=length))

    def generate_list(self, length=10, low=0, high=1000):
        return [self.random.randint(low, high) for _ in range(length)]

    def generate_dict(self, length=10, low=0, high=1000):
        return {f'key_{i}': self.random.randint(low, high) for i in range(length)}

    def generate_tuple(self, length=10, low=0, high=1000):
        return tuple(self.random.randint(low, high) for _ in range(length))

    def generate_data(self, instance):
        if isinstance(instance, int):
            return self.generate_int()
        elif isinstance(instance, float):
            return self.generate_float()
        elif isinstance(instance, str):
            return self.generate_str()
        elif isinstance(instance, list):
            return self.generate_list(length=len(instance))
        elif isinstance(instance, dict):
            return self.generate_dict(length=len(instance))
        elif isinstance(instance, tuple):
            return self.generate_tuple(length=len(instance))
        else:
            return None

if __name__ == '__main__':
    generator = RandomDataGenerator()
    data = eval(input("请输入数据："))
    random_data = generator.generate_data(data)
    print('随机生成的数据为：', random_data)

