from random_structure_function_1 import generate_random_data

def generate_structures(structure, count=10):

    for _ in range(count):
        try:
            yield generate_random_data(structure)
        except Exception as e:
            print(f"An error occurred while generating data: {e}")
            yield None 

if __name__ == "__main__":
    structure = {
        'name': {'type': 'string', 'params': {'length': 5}},
        'age': {'type': 'integer', 'params': {'min_value': 18, 'max_value': 65}},
        'gpa': {'type': 'float', 'params': {'min_value': 0.0, 'max_value': 4.0}}
    }
    for data in generate_structures(structure, count=5):
        if data is not None:
            print(data)