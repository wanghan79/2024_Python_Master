import random  # 导入随机模块
from functools import wraps  # 从functools模块导入wraps修饰器


class RandomDataGenerator:
    def __init__(self):
        pass  # 初始化方法，这里没有特别的初始化操作

    def validate_structure(func):
        @wraps(func)  # 使用wraps修饰器来保持被修饰函数的元数据
        def wrapper(self, structure, *args, **kwargs):
            # 验证传入的结构是否是有效的数据结构
            valid_types = (int, float, str, dict, list, tuple, set)
            if not isinstance(structure, valid_types):
                raise ValueError("Invalid data structure. Must be one of: int, float, str, dict, list, tuple, set.")
            return func(self, structure, *args, **kwargs)  # 调用原始函数并传递参数

        return wrapper  # 返回包装后的函数

    @validate_structure  # 使用validate_structure修饰器
    def generate_random_data(self, structure, *args, **kwargs):
        """
        根据给定的结构生成随机数据。

        参数:
            structure: 一个有效的数据结构。
            *args: 其他位置参数。
            **kwargs: 其他关键字参数。

        返回:
            一个包含基于给定结构的随机数据的列表。
        """

        def generate_random_item(item, *args, **kwargs):
            # 根据项目的数据类型生成相应的随机数据
            if isinstance(item, int):
                return random.randint(*args)
            elif isinstance(item, float):
                return random.uniform(*args)
            elif isinstance(item, str):
                return ''.join(random.choices(kwargs['charset'], k=len(item)))
            elif isinstance(item, dict):
                return {key: generate_random_item(value, *args, **kwargs) for key, value in item.items()}
            elif isinstance(item, list):
                return [generate_random_item(element, *args, **kwargs) for element in item]
            elif isinstance(item, tuple):
                return tuple(generate_random_item(element, *args, **kwargs) for element in item)
            elif isinstance(item, set):
                # 集合中的元素必须是可哈希的，避免生成列表作为集合元素
                return {generate_random_item(element, *args, **kwargs) for element in item if
                        not isinstance(element, list)}
            else:
                raise ValueError(f"Unsupported data type: {type(item)}")

        return generate_random_item(structure, *args, **kwargs)  # 生成随机数据并返回

    def generate_random_structure(self, depth=1):
        """
        生成随机数据结构。

        参数:
            depth: 数据结构的深度。

        返回:
            一个随机生成的数据结构。
        """

        def random_structure(depth):
            if depth <= 0:
                return random.choice([random.randint(0, 100), random.uniform(0, 100),
                                      ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))])

            structure_type = random.choice([dict, list, tuple, set])
            if structure_type == dict:
                return {random.choice('abcdefghijklmnopqrstuvwxyz'): random_structure(depth - 1) for _ in
                        range(random.randint(1, 5))}
            elif structure_type == list:
                return [random_structure(depth - 1) for _ in range(random.randint(1, 5))]
            elif structure_type == tuple:
                return tuple(random_structure(depth - 1) for _ in range(random.randint(1, 5)))
            elif structure_type == set:
                # 集合中的元素必须是可哈希的，避免生成列表作为集合元素
                return {random_structure(depth - 1) for _ in range(random.randint(1, 5)) if
                        not isinstance(random_structure(depth - 1), list)}

        return random_structure(depth)


# 示例用法：
generator = RandomDataGenerator()  # 创建RandomDataGenerator类的实例

# 生成随机数据结构
random_structure = generator.generate_random_structure(depth=3)
print("Random Structure:")
print(random_structure)

# 基于给定结构生成随机数据
structure = {'a': [10, 5.0, 'abc'], 'b': (1, 2, 3), 'c': {'x', 'y', 'z'}}
random_data = generator.generate_random_data(structure, 1, 100, charset='abcdefghijklmnopqrstuvwxyz')
print("\nRandom Data:")
print(random_data)
