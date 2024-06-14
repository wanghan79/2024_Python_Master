import random
import string

class StructureRandomizer:
    def __init__(self):
        pass

    def __random_value(self):
        """
        生成随机值
        :return: 随机值
        """
        return random.choice([
            random.randint(1, 100),  # 随机整数
            random.uniform(1.0, 100.0),  # 随机浮点数
            ''.join(random.choices(string.ascii_letters + string.digits, k=5)),  # 随机字符串
            None,  # None值
            True,  # 布尔值True
            False  # 布尔值False
        ])

    def randomize_structure(self, input_para):
        """
        随机化输入结构
        :param input_para: 输入结构
        :return: 随机化后的结构
        """
        if isinstance(input_para, int):
            return random.randint(1, 100)
        elif isinstance(input_para, float):
            return random.uniform(1.0, 100.0)
        elif isinstance(input_para, str):
            return ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        elif isinstance(input_para, list):
            return [self.randomize_structure(item) for item in input_para]
        elif isinstance(input_para, tuple):
            return tuple(self.randomize_structure(item) for item in input_para)
        elif isinstance(input_para, dict):
            return {key: self.randomize_structure(value) for key, value in input_para.items()}
        else:
            try:
                return self.__random_value()
            except Exception as e:
                print(f"Error occurred while randomizing structure: {e}")
                return None

# 示例调用
if __name__ == '__main__':
    randomizer = StructureRandomizer()

    input_structure = [
        {"key1": [1, 2], "key2": (3, 4)},
        (5, 6),
        [7, 8]
    ]
    b = [1, 1.2, "djgjn", input_structure]
    for i in b:
        try:
            randomized_structure = randomizer.randomize_structure(i)
            print(randomized_structure)
        except Exception as e:
            print(f"Error occurred while randomizing structure: {e}")
