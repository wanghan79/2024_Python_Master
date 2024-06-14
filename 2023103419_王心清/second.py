import random
from collections.abc import Iterable
from typing import Any, Union

class RandomStructureGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_random_number(data_type: Union[type, str]) -> Any:
        if data_type == int:
            return random.randint(0, 100)
        elif data_type == float:
            return random.uniform(0.0, 100.0)
        elif data_type == bool:
            return random.choice([True, False])
        elif data_type == str:
            return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
        else:
            raise ValueError("Unsupported data type")

    def generate(self, structure: Any) -> Any:
        if isinstance(structure, dict):
            return {key: self.generate(value) for key, value in structure.items()}
        elif isinstance(structure, list):
            return [self.generate(item) for item in structure]
        elif isinstance(structure, tuple):
            return tuple(self.generate(item) for item in structure)
        elif isinstance(structure, set):
            return {self.generate(item) for item in structure}
        elif isinstance(structure, Iterable) and not isinstance(structure, (str, bytes)):
            return type(structure)(self.generate(item) for item in structure)
        else:
            return self.generate_random_number(structure)


if __name__ == "__main__":
    generator = RandomStructureGenerator()
    input_structure = {"UID": int, "Character": [float, {"Name": str, "Type": bool}], "other": (int, bool)}
    output_structure = generator.generate(input_structure)
    print(output_structure)