import random


class RandomStructureGenerator:
    """
    随机结构生成器类，根据传入的结构定义生成随机数据样本列表。
    """
    def __init__(self, num, struct):
        """
        初始化随机结构生成器。
        """
        self.num = num
        self.struct = struct

    def generate_samples(self):
        """
        生成随机数据样本列表。
        """
        result = []

        # 检查样本数量参数是否为非负整数
        if not isinstance(self.num, int) or self.num < 0:
            raise ValueError("Parameter 'num' must be a non-negative integer!")

        # 检查结构参数是否为字典类型
        if not isinstance(self.struct, dict):
            raise TypeError("Parameter 'struct' must be a dictionary!")

        # 生成指定数量的样本
        for _ in range(self.num):
            # 初始化每个样本的元素字典
            element = {}
            for key, value in self.struct.items():
                # 根据数据类型生成随机数或随机字符串
                if value['datatype'] == 'int':
                    element[key] = random.randint(*value['datarange'])
                elif value['datatype'] == 'float':
                    element[key] = random.uniform(*value['datarange'])
                elif value['datatype'] == 'str':
                    element[key] = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value.get('len', 1)))
                elif value['datatype'] == 'struct':
                    # 递归调用generate_samples生成嵌套结构
                    nested_generator = RandomStructureGenerator(num=1, struct=value['datarange'])
                    element[key] = nested_generator.generate_samples()[0]
                else:
                    raise ValueError(f"Unsupported datatype '{value['datatype']}' for field '{key}'")

            result.append(element)  # 将生成的样本字典添加到结果列表中

        return result  # 返回生成的样本列表


def run():
    """
    执行示例函数，使用RandomStructureGenerator生成随机数据样本并打印。
    """
    sample_structure = {
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

    generator = RandomStructureGenerator(num=10, struct=sample_structure)
    samples = generator.generate_samples()

    print("Generated Samples:")
    for sample in samples:
        print(sample)


# 如果作为独立脚本运行，执行示例函数
if __name__ == "__main__":
    run()
