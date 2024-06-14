import random

class RandomStructureGenerator:
    def __init__(self):
        self._logger = []

    def log(self, message):
        self._logger.append(message)

    def get_logs(self):
        return self._logger

    def generate_random_value(self, type_hint):
        """
        生成指定类型的随机数
        """
        if type_hint is int:
            return random.randint(0, 100)
        elif type_hint is float:
            return random.uniform(0, 1)
        elif type_hint is str:
            return ''.join(
                random.choice('abcdefghijklmnopqrstuvwxyz')
                for _ in range(6)
            )
        elif type_hint is bool:
            return random.choice([True, False])
        else:
            raise ValueError(f"Unsupported data type: {type_hint}")

    def generate_random_structure(self, structure):
        """
        递归生成与输入结构相同的随机数结构
        """
        if isinstance(structure, (int, float, str, bool)):
            value = self.generate_random_value(type(structure))
            self.log(f"Generated value: {value}")
            return value
        elif isinstance(structure, list):
            self.log("Generating list")
            return [
                self.generate_random_structure(item)
                for item in structure
            ]
        elif isinstance(structure, dict):
            self.log("Generating dict")
            return {
                key: self.generate_random_structure(value)
                for key, value in structure.items()
            }
        else:
            raise ValueError(f"Unsupported data structure: {structure}")

# 测试
test_structure = [
    1, 2.0, "string", True,
    [1, 2, [3, 4]],
    {"a": 1, "b": [1, 2, 3]}
]

generator = RandomStructureGenerator()
random_structure = generator.generate_random_structure(test_structure)

print("Generated Random Structure:")
print(random_structure)
print("\nLogs:")
print(generator.get_logs())
