
import random

def generate_random_structure(num_elements):
    structure = []

    # Generate a random structure here
    for _ in range(num_elements):
        element = {
            "name": "Element_" + str(_),
            "value": random.randint(1, 100),
            "description": "Random Description"
        }
        structure.append(element)

    return structure

# Example usage
num_elements = 5
random_structure = generate_random_structure(num_elements)
for element in random_structure:
    print(element)
