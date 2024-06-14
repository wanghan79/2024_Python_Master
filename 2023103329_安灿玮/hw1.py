# hw1.py
import random


def generate_random_structure(**kwargs):
    """
    根据传入的结构定义生成随机数据样本列表。
    """
    result = []

    # 获取样本数量参数，如果没有提供则抛出异常
    n = kwargs.get('num', -1)
    if n == -1:
        raise Exception('Missing Parameter: num!')

    # 获取结构参数，如果没有提供则抛出异常
    struct = kwargs.get('struct', None)
    if struct is None:
        raise Exception('Missing Parameter: struct!')

    # 生成指定数量的样本
    for _ in range(n):
        # 初始化每个样本的元素列表
        element = []
        for key, value in struct.items():
            # 根据数据类型生成随机数或随机字符串
            if value['datatype'] == 'int':
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif value['datatype'] == 'float':
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif value['datatype'] == 'str':
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            elif value['datatype'] == 'struct':
                # 递归调用generate_random_structure生成嵌套结构
                tmp = generate_random_structure(num=1, struct=value['datarange'])[0]
            else:
                break  # 如果数据类型不支持，退出循环
            element.append(tmp)  # 将生成的随机值添加到元素列表中
        result.append(element)  # 将每个样本的元素列表添加到结果列表中

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
        }}
    }

    samples = generate_random_structure(num=10, struct=sample_structure)
    print("Generated Samples:")
    for sample in samples:
        print(sample)


# 如果作为独立脚本运行，执行示例函数
if __name__ == "__main__":
    run()
