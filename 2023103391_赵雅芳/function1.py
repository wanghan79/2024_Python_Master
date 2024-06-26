import random
import string


def generate_random_element(types=None):
    """
    生成随机元素，可以是int，float，str，list，tuple，dict。

    :param types: 一个包含期望类型的列表。如果为None，则随机选择一个类型。
    :return: 一个随机元素。
    """
    if types is None:
        types = random.choice([int, float, str, list, tuple, dict])

    if types == int:
        return random.randint(0, 100)
    elif types == float:
        return random.uniform(0.0, 100.0)
    elif types == str:
        return ''.join(random.choices(string.ascii_letters, k=random.randint(1, 10)))
    elif types == list:
        return [generate_random_element(types=None) for _ in range(random.randint(1, 5))]
    elif types == tuple:
        return tuple(generate_random_element(types=None) for _ in range(random.randint(1, 5)))
    elif types == dict:
        return {
            random.choice(string.ascii_letters): generate_random_element(types=None)
            for _ in range(random.randint(1, 5))
        }
    else:
        raise ValueError("Unsupported type specified.")


def generate_random_structure(depth=3, max_size=10, structure_template=None):
    """
    生成具有嵌套结构的随机数列表。

    :param depth: 嵌套深度，默认是3层。
    :param max_size: 每个节点最大大小，默认是10。
    :param structure_template: 一个字典， specifying the structure of the generated data.
                               If None, a random element is generated.
    :return: 一个嵌套的随机数列表。
    """
    if depth <= 0:
        if structure_template is not None:
            return generate_random_element(types=structure_template['type'])
        else:
            return generate_random_element(types=None)  # 如果深度为0，则返回一个随机元素

    # 随机选择一个操作：生成元素或列表
    if random.choice([True, False]):
        if structure_template is not None:
            return generate_random_element(types=structure_template['type'])
        else:
            return generate_random_element(types=None)  # 生成一个随机元素
    else:
        return [generate_random_structure(depth - 1, max_size, structure_template) for _ in
                range(random.randint(1, max_size))]  # 生成一个随机长度的列表


# 示例结构模板
structure_template = {
    'type': random.choice([int, float, str, list, tuple, dict])
}
# 测试函数
random_structure = generate_random_structure(depth=2, max_size=5, structure_template=structure_template)
print(random_structure)