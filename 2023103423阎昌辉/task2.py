import random


# 生成随机值
def generate_random_value(data_type):
    if data_type == int:
        return random.randint(1, 100)
    elif data_type == float:
        return random.uniform(1, 100)
    elif data_type == str:
        return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    elif data_type == bool:
        return random.choice([True, False])
    else:
        return None


# 使用类封装生成随机数
class RandomDataGenerator:
    def __init__(self):
        self.random_value = None

    def generate(self, data_structure):
        self.random_value = self._generate_random_data(data_structure)
        return self.random_value

    def _generate_random_data(self, data_structure):
        if isinstance(data_structure, list):
            return [self._generate_random_data(item) for item in data_structure]
        elif isinstance(data_structure, tuple):
            return tuple(self._generate_random_data(item) for item in data_structure)
        elif isinstance(data_structure, dict):
            return {key: self._generate_random_data(value) for key, value in data_structure.items()}
        else:
            return self._generate_random_value(data_structure)

    def _generate_random_value(self, data_type):
        if data_type == int:
            return random.randint(1, 100)
        elif data_type == float:
            return random.uniform(1, 100)
        elif data_type == str:
            return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
        elif data_type == bool:
            return random.choice([True, False])
        else:
            return None


# 示例用法
data_structure = [int, [str, bool], {'key': float}]
generator = RandomDataGenerator()
random_data = generator.generate(data_structure)
print(random_data)
