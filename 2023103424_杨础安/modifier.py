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
                return random.randint(*args)  # 生成一个随机整数
            elif isinstance(item, float):
                return random.uniform(*args)  # 生成一个随机浮点数
            elif isinstance(item, str):
                return ''.join(random.choices(kwargs['charset'], k=len(item)))  # 从给定字符集中生成随机字符串
            elif isinstance(item, dict):
                return {key: generate_random_item(value, *args, **kwargs) for key, value in item.items()}  # 递归生成随机字典
            elif isinstance(item, list):
                return [generate_random_item(element, *args, **kwargs) for element in item]  # 递归生成随机列表
            elif isinstance(item, tuple):
                return tuple(generate_random_item(element, *args, **kwargs) for element in item)  # 递归生成随机元组
            elif isinstance(item, set):
                return {generate_random_item(element, *args, **kwargs) for element in item}  # 递归生成随机集合
            else:
                raise ValueError(f"Unsupported data type: {type(item)}")  # 如果数据类型不支持，抛出异常

        return generate_random_item(structure, *args, **kwargs)  # 生成随机数据并返回


# 示例用法：
structure = {'a': [10, 5.0, 'abc', True], 'b': (1, 2, 3), 'c': {'x', 'y', 'z'}}
generator = RandomDataGenerator()  # 创建RandomDataGenerator类的实例
random_data = generator.generate_random_data(structure, 1, 100, charset='abcdefghijklmnopqrstuvwxyz')  # 生成随机数据
print(random_data)  # 打印生成的随机数据
