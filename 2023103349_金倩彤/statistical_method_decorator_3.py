from random_structure_class_2 import DataGenerator
import numpy as np

def statistics(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        numeric_values = [v for v in data.values() if isinstance(v, (int, float))]
        if numeric_values:
            return {
                'sum': sum(numeric_values),
                'mean': np.mean(numeric_values)
            }
        else:
            return {}
    return wrapper

class StatisticDataGenerator(DataGenerator):
    @staticmethod
    @statistics
    def generate_random_data(structure):
        return DataGenerator.generate_random_data(structure)

if __name__ == "__main__":
    structure = {'name': {'type': 'string', 'params': {'length': 10}}, 'age': {'type': 'integer', 'params': {'min_value': 18, 'max_value': 30}}}
    stats_generator = StatisticDataGenerator()
    print(stats_generator.generate_random_data(structure))