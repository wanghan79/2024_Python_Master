import random

class RandomStructureGenerator:
    def __init__(self):
        self._logger = []

    def log(self, message):
        self._logger.append(message)

    def get_logs(self):
        return self._logger

    def generate_random_value(self, type_hint):
        """生成指定类型的随机数"""
        if type_hint == int:
            return random.randint(0, 100)
        elif type_hint == float:
            return random.random()
        elif type_hint == str:
            return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5))
        elif type_hint == bool:
            return random.choice([True, False])
        else:
            raise ValueError(f"Unsupported data type: {type_hint}")

    def generate_random_structure(self, structure):
        """递归生成与输入结构相同的随机数结构"""
        if isinstance(structure, (int, float, str, bool)):
            return self.generate_random_value(type(structure))
        elif isinstance(structure, list):
            return [self.generate_random_structure(item) for item in structure]
        elif isinstance(structure, dict):
            return {key: self.generate_random_structure(value) for key, value in structure.items()}
        else:
            raise ValueError(f"Unsupported data structure: {structure}")


test_structure = [1, 3.0, "string", True, [1, 2, [3, 4,5]], {"a": 1, "b": [1, 2, 3]}]
generator = RandomStructureGenerator()
random_structure = generator.generate_random_structure(test_structure)

print("Generated Random Structure:")
print(random_structure)

