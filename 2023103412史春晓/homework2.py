import random
import string
import numpy as np

class DataProcessor:
    def __init__(self, **kwargs):
        self.config = kwargs

    def generate_random_value(self, data_type):
        if data_type == 'int':
            return random.randint(self.config.get('int_min', 1), self.config.get('int_max', 100))
        elif data_type == 'float':
            return random.uniform(self.config.get('float_min', 0.1), self.config.get('float_max', 100.0))
        elif data_type == 'str':
            length = self.config.get('str_len', 10)
            chars = self.config.get('str_chars', string.ascii_letters + string.digits)
            return ''.join(random.choices(chars, k=length))
        else:
            raise ValueError(f"Unsupported data type: {data_type}")

    def generate_data(self, structure):
        if isinstance(structure, dict):
            return {key: self.generate_data(value) for key, value in structure.items()}
        elif isinstance(structure, list):
            return [self.generate_data(item) for item in structure]
        elif isinstance(structure, str):
            return self.generate_random_value(structure)
        else:
            return structure

    def process_data(self, data, *operations):
        """处理数据，并根据操作参数返回相应的结果，支持求和、均值等操作。"""
        results = []
        if 'sum' in operations:
            results.append(np.sum(data))
        if 'mean' in operations:
            results.append(np.mean(data))
        if 'std' in operations:
            results.append(np.std(data))
        return results

if __name__ == '__main__':
    processor = DataProcessor(int_min=10, int_max=500, float_min=0.1, float_max=50.0, str_len=8)
    data_structure = {
        'values': ['int', 'int', 'int', 'float']
    }

    random_data = processor.generate_data(data_structure)
    print("Generated Data:", random_data)

    results = processor.process_data(random_data['values'], 'sum', 'mean', 'std')
    print("Processed Results:", results)
