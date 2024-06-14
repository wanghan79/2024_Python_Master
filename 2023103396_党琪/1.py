import random

def generate_random_structure(structure):
    if isinstance(structure, list):
        return [generate_random_structure(item) for item in structure]
    elif isinstance(structure, dict):
        return {key: generate_random_structure(value) for key, value in structure.items()}
    elif isinstance(structure, int):
        return random.randint(0, structure)
    elif isinstance(structure, float):
        return random.uniform(0, structure)
    elif isinstance(structure, str):
        return ''.join(random.choice(structure) for _ in range(len(structure)))
    else:
        raise ValueError("Unsupported data type")

# Test
input = [1, 2.0, "wer"]
output = generate_random_structure(input)
print(output)