import random
import string

class RandomStructureGenerator:
    def __init__(self):
        pass

    def generate_random_value(self, value_type):
        if value_type == int:
            return random.randint(0, 100)
        elif value_type == float:
            return random.uniform(0, 100)
        elif value_type == str:
            # 使用 random.sample 来生成一个随机字符串
            return ''.join(random.sample(string.ascii_letters + string.digits, 8))
        elif value_type == bool:
            return random.choice([True, False])
        else:
            raise ValueError("Unsupported value type: {}".format(value_type))

    def generate_random_structure(self, structure):
        if isinstance(structure, dict):
            return {k: self.generate_random_structure(v) for k, v in structure.items()}
        elif isinstance(structure, list):
            return [self.generate_random_structure(elem) for elem in structure]
        elif isinstance(structure, tuple):
            return tuple(self.generate_random_structure(elem) for elem in structure)
        elif isinstance(structure, set):
            return {self.generate_random_structure(elem) for elem in structure}
        elif isinstance(structure, type):  # Check if it's a type
            return self.generate_random_value(structure)
        else:
            raise ValueError("Unsupported structure type: {}".format(type(structure)))

# Example usage
if __name__ == "__main__":
    generator = RandomStructureGenerator()
    input_structure = {
        'a': int,
        'b': [float, str],
        'c': {'d': bool, 'e': int},
        'f': (str, float)
    }
    print(generator.generate_random_structure(input_structure))
