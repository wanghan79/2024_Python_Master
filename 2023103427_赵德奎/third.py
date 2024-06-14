import random
from typing import Any, Union, Dict, List, Tuple


def call_counter(func):
    """Decorator to count the number of times a function is called."""
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper


class RandomStructureGenerator:
    def __init__(self):
        pass

    @call_counter
    def generate(self, structure: Any) -> Any:
        """Generates random data based on the input structure."""
        if isinstance(structure, dict):
            return {key: self.generate(value) for key, value in structure.items()}
        elif isinstance(structure, list):
            return [self.generate(item) for item in structure]
        elif isinstance(structure, tuple):
            return tuple(self.generate(item) for item in structure)
        else:
            return self.generate_random_value(structure)

    def generate_random_value(self, data_type: Union[type, str]) -> Any:
        """Generates a random value based on the specified data type."""
        if data_type == int:
            return random.randint(0, 100)
        elif data_type == float:
            return round(random.uniform(0.0, 100.0), 2)
        elif data_type == bool:
            return random.choice([True, False])
        elif data_type == str:
            return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
        else:
            raise ValueError("Unsupported data type")


if __name__ == "__main__":
    generator = RandomStructureGenerator()

    # Example input structure
    input_structure = {
        "UID": int,
        "Character": [
            float,
            {"Name": str, "Type": bool}
        ],
        "other": (int, bool)
    }

    # Generate random data based on the input structure
    output_structure = generator.generate(input_structure)
    
    # Print the generated output structure
    print(output_structure)
    
    # Print the number of times the generate method was called
    print(f"generate() method was called {generator.generate.call_count} times.")
