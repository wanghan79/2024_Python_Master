import random
import string

class RandomDataGenerator:
    def __init__(self):
        self.data_types = {
            "int": self.generate_random_int,
            "float": self.generate_random_float,
            "str": self.generate_random_str
        }

    def generate_random_int(self):
        return random.randint(0, 100)

    def generate_random_float(self):
        return random.uniform(0, 10000)

    def generate_random_str(self):
        length = random.randint(1, 10)
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    def generate_random_data(self, data_type):
        if data_type in self.data_types:
            return self.data_types[data_type]()
        else:
            return None

    def generate_random_structure(self, structure):
        if isinstance(structure, str):
            return self.generate_random_data(structure)
        elif isinstance(structure, list):
            return [self.generate_random_structure(item) for item in structure]
        elif isinstance(structure, tuple):
            return tuple(self.generate_random_structure(item) for item in structure)
        elif isinstance(structure, dict):
            return {key: self.generate_random_structure(value) for key, value in structure.items()}
        else:
            return None

# Example usage
data_structure = {
    "name": "str",
    "age": "int",
    "scores": ["int", "int", "int"],
    "info": {
        "city": "str",
        "email": "str"
    }
}

generator = RandomDataGenerator()
random_data = generator.generate_random_structure(data_structure)
print(random_data)
