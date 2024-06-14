import random


def generate_random_structure(**kwargs):
    """
    根据传入的结构定义生成随机数据样本列表。
    """
    result = []

    # 检查并获取样本数量参数，如果没有提供则抛出异常
    try:
        n = kwargs['num']
    except KeyError:
        raise ValueError("Missing parameter 'num'!")

    # 检查样本数量参数是否为非负整数
    if not isinstance(n, int) or n < 0:
        raise ValueError("Parameter 'num' must be a non-negative integer!")

    # 检查并获取结构参数，如果没有提供或不是字典类型则抛出异常
    try:
        struct = kwargs['struct']
    except KeyError:
        raise ValueError("Missing parameter 'struct'!")
    if not isinstance(struct, dict):
        raise TypeError("Parameter 'struct' must be a dictionary!")

    # 生成指定数量的样本
    for _ in range(n):
        # 初始化每个样本的元素字典
        element = {}
        for key, value in struct.items():
            # 根据数据类型生成随机数或随机字符串
            if value['datatype'] == 'int':
                element[key] = random.randint(*value['datarange'])
            elif value['datatype'] == 'float':
                element[key] = random.uniform(*value['datarange'])
            elif value['datatype'] == 'str':
                element[key] = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value.get('len', 1)))
            elif value['datatype'] == 'struct':
                # 递归调用generate_random_structure生成嵌套结构
                element[key] = generate_random_structure(num=1, struct=value['datarange'])[0]
            else:
                raise ValueError(f"Unsupported datatype '{value['datatype']}' for field '{key}'")

        result.append(element)  # 将生成的样本字典添加到结果列表中

    return result  # 返回生成的样本列表


def run():
    """
    执行示例函数，生成随机数据样本并打印。
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

    # 生成10个样本
    samples = generate_random_structure(num=10, struct=sample_structure)
    print("Generated Samples:")
    for sample in samples:
        print(sample)


# 如果作为独立脚本运行，执行示例函数
if __name__ == "__main__":
    run()
