import random

class RandomDataGenerator:
    def __init__(self):
        self.type_generators = {
            int: self.generate_random_int,
            float: self.generate_random_float,
            str: self.generate_random_str,
            bool: self.generate_random_bool,
            list: self.generate_random_list,
            dict: self.generate_random_dict
        }

    def generate_random_int(self):
        return random.randint(0, 100)

    def generate_random_float(self):
        return random.random()

    def generate_random_str(self):
        return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5))

    def generate_random_bool(self):
        return random.choice([True, False])

    def generate_random_list(self, length=5):
        return [self.generate_random_value(int) for _ in range(length)]

    def generate_random_dict(self, num_items=3):
        return {self.generate_random_str(): self.generate_random_value(int) for _ in range(num_items)}

    def generate_random_value(self, type_hint):
        if type_hint in self.type_generators:
            return self.type_generators[type_hint]()
        else:
            raise ValueError(f"Unsupported data type: {type_hint}")

    def generate_random_structure(self, structure):
        if isinstance(structure, (int, float, str, bool)):
            return self.generate_random_value(type(structure))
        elif isinstance(structure, list):
            return [self.generate_random_structure(item) for item in structure]
        elif isinstance(structure, dict):
            return {key: self.generate_random_structure(value) for key, value in structure.items()}
        else:
            raise ValueError(f"Unsupported data structure: {structure}")

# 测试
test_structure = [1, 2.0, "string", True, [1, "abc", [3, 4]], {"a": 1, "b": [1, 2, 3, "xyz"]}]

generator = RandomDataGenerator()
result = generator.generate_random_structure(test_structure)
print(result)
