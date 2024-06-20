# test_2.py
import random

class RandomStructureGenerator:
    """
    随机结构生成器类。
    """
    def __init__(self, num, struct):
        """
        初始化生成器。
        """
        self.num = num
        self.struct = struct

    def generate_samples(self):
        """
        生成随机数据样本列表。
        """
        samples = []

        if not isinstance(self.num, int) or self.num < 0:
            raise ValueError("参数 'num' 必须是非负整数!")

        if not isinstance(self.struct, dict):
            raise TypeError("参数 'struct' 必须是字典类型!")

        for _ in range(self.num):
            sample = {}
            for key, value in self.struct.items():
                if value['datatype'] == 'int':
                    sample[key] = random.randint(*value['datarange'])
                elif value['datatype'] == 'float':
                    sample[key] = random.uniform(*value['datarange'])
                elif value['datatype'] == 'str':
                    sample[key] = ''.join(random.choices(value['datarange'], k=value.get('len', 1)))
                elif value['datatype'] == 'struct':
                    nested_generator = RandomStructureGenerator(num=1, struct=value['datarange'])
                    sample[key] = nested_generator.generate_samples()[0]
                else:
                    raise ValueError(f"不支持的数据类型 '{value['datatype']}' 在字段 '{key}'")

            samples.append(sample)

        return samples

def run():
    """
    示例函数，使用RandomStructureGenerator生成随机数据样本并打印。
    """
    structure = {
        "field1": {"datatype": "int", "datarange": (1, 100)},
        "field2": {"datatype": "float", "datarange": (0.0, 1.0)},
        "field3": {"datatype": "str", "datarange": "abcdefghijklmnopqrstuvwxyz", "len": 5},
        "field4": {"datatype": "struct", "datarange": {
            "nested1": {"datatype": "int", "datarange": (100, 200)},
            "nested2": {"datatype": "str", "datarange": "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "len": 3}
        }},
        "field5": {"datatype": "struct", "datarange": {
            "nested3": {"datatype": "float", "datarange": (50.0, 100.0)},
            "nested4": {"datatype": "str", "datarange": "!@#$%^&*()_+", "len": 4}
        }}
    }

    generator = RandomStructureGenerator(num=10, struct=structure)
    samples = generator.generate_samples()

    print("生成的样本:")
    for sample in samples:
        print(sample)

if __name__ == "__main__":
    run()