import random


class RandomStructureGenerator:
    def __init__(self, num_elements):
        self.num_elements = num_elements
        self.structure = []

    def generate_structure(self):
        for i in range(self.num_elements):
            element = {
                "name": f"Element_{i}",
                "value": random.randint(1, 100),
                "description": "Random Description"
            }
            self.structure.append(element)

    def get_structure(self):
        return self.structure


# Example usage
num_elements = 5
generator = RandomStructureGenerator(num_elements)
generator.generate_structure()
random_structure = generator.get_structure()

for element in random_structure:
    print(element)
