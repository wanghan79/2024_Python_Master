import random
import string

class RandomStructureGenerator:
    def __init__(self):
        self.random = random.Random()

    def generate(self, structure):
        if isinstance(structure, list):
            return [self.generate(item) for item in structure]
        elif isinstance(structure, dict):
            return {key: self.generate(value) for key, value in structure.items()}
        elif isinstance(structure, int):
            return self.random.randint(1, structure)
        elif isinstance(structure, float):
            return self.random.uniform(0, structure)
        elif isinstance(structure, str):
            return ''.join(self.random.choice(string.ascii_lowercase) for _ in range(len(structure)))
        else:
            raise ValueError("Unsupported data type")

# 定义数据结构
data_structure_template = {
    "int_list": [10],  # 一个包含10个随机整数的列表
    "float_dict": {"values": 3},  # 一个包含3个随机浮点数的字典
    "string_length": 10,  # 一个长度为10的随机字符串
    "nested_structure": {
        "nested_list": [2],  # 嵌套结构中的列表，包含2个元素
        "nested_int": 1  # 嵌套结构中的整数
    }
}

generator = RandomStructureGenerator()
random_data_structure = generator.generate(data_structure_template)

# 打印
def print_structure(data, indent=0):
    for key, value in data.items():
        print('    ' * indent + str(key) + ':', end=' ')
        if isinstance(value, dict):
            print()
            print_structure(value, indent + 1)
        else:
            print(value)

print_structure(random_data_structure)