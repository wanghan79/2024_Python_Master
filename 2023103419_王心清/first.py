import random
from collections.abc import Iterable
from typing import Any, Union

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

def generate_random_structure(structure: Any) -> Any:
    if isinstance(structure, dict):
        return {key: generate_random_structure(value) for key, value in structure.items()}
    elif isinstance(structure, list):
        return [generate_random_structure(item) for item in structure]
    elif isinstance(structure, tuple):
        return tuple(generate_random_structure(item) for item in structure)
    elif isinstance(structure, set):
        return {generate_random_structure(item) for item in structure}
    elif isinstance(structure, Iterable) and not isinstance(structure, (str, bytes)):
        return type(structure)(generate_random_structure(item) for item in structure)
    else:
        return generate_random_number(structure)


if __name__ == "__main__":
    input_structure = {"UID": int, "Character": [float, {"Name": str, "Type": bool}], "other": (int, bool)}
    output_structure = generate_random_structure(input_structure)
    print(output_structure)