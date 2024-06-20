# test_1.py
import random

def generate_random_structure(**kwargs):
    """
    生成随机数据结构的函数。
    """
    samples = []

    try:
        num_samples = kwargs['num']
    except KeyError:
        raise ValueError("参数 'num' 缺失!")

    if not isinstance(num_samples, int) or num_samples < 0:
        raise ValueError("参数 'num' 必须是非负整数!")

    try:
        structure = kwargs['struct']
    except KeyError:
        raise ValueError("参数 'struct' 缺失!")
    if not isinstance(structure, dict):
        raise TypeError("参数 'struct' 必须是字典类型!")

    for _ in range(num_samples):
        sample = {}
        for key, value in structure.items():
            if value['datatype'] == 'int':
                sample[key] = random.randint(*value['datarange'])
            elif value['datatype'] == 'float':
                sample[key] = random.uniform(*value['datarange'])
            elif value['datatype'] == 'str':
                sample[key] = ''.join(random.choices(value['datarange'], k=value.get('len', 1)))
            elif value['datatype'] == 'struct':
                sample[key] = generate_random_structure(num=1, struct=value['datarange'])[0]
            else:
                raise ValueError(f"不支持的数据类型 '{value['datatype']}' 在字段 '{key}'")

        samples.append(sample)

    return samples

def run():
    """
    示例函数，生成随机数据样本并打印。
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

    samples = generate_random_structure(num=10, struct=structure)
    print("生成的样本:")
    for sample in samples:
        print(sample)

if __name__ == "__main__":
    run()