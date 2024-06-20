import random

#将函数封装到类里面 然后进行下面的测试

class RandomDataGenerator:
    def generate_data(self, data_type):
        if data_type == 'int':
            return random.randint(0, 10)
        elif data_type == 'float':
            return random.uniform(0.0, 100.0)
        elif data_type == 'str':
            return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
        elif data_type == 'list':
            return [random.randint(0, 100) for _ in range(5)]
        elif data_type == 'dict':
            return {f'key_{i}': random.randint(0, 100) for i in range(5)}
        else:
            return None

# Example usage:
if __name__ == "__main__":
    generator = RandomDataGenerator()
    data_type = input("请输入数据类型（int、float、str、list、dict）：")
    random_data = generator.generate_data(data_type)
    print('随机生成的数据为：', random_data)
