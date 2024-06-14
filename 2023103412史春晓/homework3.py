import random
import string
import numpy as np

def statistical_operations(*stats_funcs):
    def decorator(func):
        def wrapper(self, data, *args, **kwargs):
            results = func(self, data, *args, **kwargs)
            stats = {}
            for stat_func in stats_funcs:
                stat_name = stat_func.__name__
                try:
                    stats[stat_name] = stat_func(data)
                except Exception as e:
                    stats[stat_name] = f"Error calculating {stat_name}: {str(e)}"
            return results, stats
        return wrapper
    return decorator

class DataProcessor:
    def __init__(self, **kwargs):
        self.config = kwargs

    def generate_random_value(self, data_type):
        if data_type == int:
            return random.randint(self.config.get('int_min', 1), self.config.get('int_max', 100))
        elif data_type == float:
            return random.uniform(self.config.get('float_min', 0.1), self.config.get('float_max', 100.0))
        elif data_type == str:
            length = self.config.get('str_len', 10)
            chars = self.config.get('str_chars', string.ascii_letters + string.digits)
            return ''.join(random.choices(chars, k=length))
        elif data_type == bool:
            return random.choice([True, False])
        else:
            raise ValueError(f"Unsupported data type: {data_type}")

    def generate_data(self, structure):
        if isinstance(structure, dict):
            return {key: self.generate_data(value) for key, value in structure.items()}
        elif isinstance(structure, list):
            return [self.generate_data(item) for item in structure]
        elif isinstance(structure, str):
            try:
                data_type = eval(structure)
                if data_type in [int, float, str, bool]:
                    return self.generate_random_value(data_type)
            except NameError:
                raise ValueError(f"Unsupported data type name: {structure}")
        else:
            raise ValueError(f"Unsupported data structure: {structure}")

    @statistical_operations(np.sum, np.mean, np.std)
    def process_data(self, data):
        return data

if __name__ == '__main__':
    processor = DataProcessor(int_min=10, int_max=100, float_min=1.0, float_max=10.0, str_len=8)
    data_structure = ['int', 'float', 'int', 'int']
    random_data = processor.generate_data(data_structure)
    print("Generated Data:", random_data)

    data_results, statistics = processor.process_data(random_data)
    print("Data Results:", data_results)
    print("Statistics:", statistics)
