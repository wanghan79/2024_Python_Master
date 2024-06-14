# hw2.py
import random


class RandomStructureGenerator:
    def __init__(self, num, struct):
        self.num = num
        self.struct = struct

    def generate_random_structure(self):
        """
        根据结构定义生成随机数据样本列表。
        """
        result = []

        for _ in range(self.num):
            element = []
            for key, value in self.struct.items():
                if value['datatype'] == 'int':
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it), next(it))
                elif value['datatype'] == 'float':
                    it = iter(value['datarange'])
                    tmp = random.uniform(next(it), next(it))
                elif value['datatype'] == 'str':
                    tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
                elif value['datatype'] == 'struct':
                    nested_generator = RandomStructureGenerator(num=1, struct=value['datarange'])
                    tmp = nested_generator.generate_random_structure()[0]
                else:
                    break
                element.append(tmp)
            result.append(element)

        return result

    def run(self):
        """
        执行示例函数，生成随机数据样本并打印。
        """
        samples = self.generate_random_structure()
        print("Generated Samples:")
        for sample in samples:
            print(sample)


# 如果作为独立脚本运行，执行示例函数
if __name__ == "__main__":
    sample_structure = {
        "field1": {"datatype": "int", "datarange": (1, 100)},
        "field2": {"datatype": "float", "datarange": (0.0, 1.0)},
        "field3": {"datatype": "str", "datarange": "abcdefghijklmnopqrstuvwxyz", "len": 5},
        "field4": {"datatype": "struct", "datarange": {
            "nested1": {"datatype": "int", "datarange": (100, 200)},
            "nested2": {"datatype": "str", "datarange": "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "len": 3}
        }}
    }

    generator = RandomStructureGenerator(num=10, struct=sample_structure)
    generator.run()
