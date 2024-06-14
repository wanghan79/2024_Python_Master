from random_structure_function_1 import random_string, random_integer, random_float, random_phone_number, generate_random_data

class DataGenerator:
    @staticmethod
    def generate_random_data(structure):
        return generate_random_data(structure)

if __name__ == "__main__":
    structure = {'name': {'type': 'string', 'params': {'length': 5}}}
    generator = DataGenerator()
    print(generator.generate_random_data(structure))