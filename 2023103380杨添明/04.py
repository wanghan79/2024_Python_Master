import random

def random_structure_generator():
    while True:
        # Generate a random structure here, for example:
        structure = [random.randint(1, 10) for _ in range(5)]  # Example: Generate a list of 5 random integers
        yield structure

# Example usage
generator = random_structure_generator()

# Generate 5 random structures
for _ in range(5):
    structure = next(generator)
    print(f"Generated structure: {structure}")
