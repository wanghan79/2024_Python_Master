import random
import string
from functools import wraps

class StructureRandomizer:
    def __init__(self):
        pass

    def __random_value(self):
        """
        生成随机值
        :yield: 随机值
        """
        yield random.randint(1, 100)  # 随机整数
        yield random.uniform(1.0, 100.0)  # 随机浮点数
        yield ''.join(random.choices(string.ascii_letters + string.digits, k=5))  # 随机字符串
        yield None  # None值
        yield True  # 布尔值True
        yield False  # 布尔值False

    def randomize_structure(self, func):
        """
        随机化输入结构
        :param func: 处理输入结构的函数
        :return: 随机化后的结构
        """
        @wraps(func)
        def wrapper(input_para):
            if isinstance(input_para, int):
                return random.randint(1, 100)
            elif isinstance(input_para, float):
                return random.uniform(1.0, 100.0)
            elif isinstance(input_para, str):
                return ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            elif isinstance(input_para, list):
                return [self.randomize_structure(lambda x: x)(x) for x in input_para]
            elif isinstance(input_para, tuple):
                return tuple(self.randomize_structure(lambda x: x)(x) for x in input_para)
            elif isinstance(input_para, dict):
                return {key: self.randomize_structure(lambda x: x)(value) for key, value in input_para.items()}
            else:
                try:
                    return next(self.__random_value())
                except Exception as e:
                    print(f"Error occurred while randomizing structure: {e}")
                    return None
        return wrapper

# 示例调用
if __name__ == '__main__':
    randomizer = StructureRandomizer()

    @randomizer.randomize_structure
    def process_input(input_para):
        return input_para

    input_structure = [
        {"key1": [1, 2], "key2": (3, 4)},
        (5, 6),
        [7, 8]
    ]
    b = [1, 1.2, "djgjn", input_structure]
    for i in b:
        try:
            randomized_structure = process_input(i)
            print(randomized_structure)
        except Exception as e:
            print(f"Error occurred while randomizing structure: {e}")
