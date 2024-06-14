from faker import Faker
import random

class DataProcessor:
    """Class for generating and processing content based on input data structures."""

    def __init__(self):
        self.faker = Faker()

    def generate(self, quantity, data_type, operation=None, **elements):
        """Generates data according to a specified data structure and computes statistics if needed."""

        def recursively_parse(data):
            if isinstance(data, dict):
                return {key: recursively_parse(value) for key, value in data.items()}
            elif isinstance(data, list):
                return [recursively_parse(item) for item in data]
            elif isinstance(data, tuple):
                return tuple(recursively_parse(item) for item in data)
            else:
                return data

        results = []
        numerical_values = []

        for _ in range(quantity):
            parsed_data = recursively_parse(elements)
            if data_type == 'string':
                processed_data = ''.join(map(str, parsed_data.values()))
            elif data_type == 'list':
                processed_data = list(parsed_data.values())
            elif data_type == 'dict':
                processed_data = parsed_data
            elif data_type == 'tuple':
                processed_data = tuple(parsed_data.values())

            results.append(processed_data)
            numerical_values.extend(self.extract_numerical_values(parsed_data))

        if operation:
            statistical_result = self.calculate_statistic(numerical_values, operation)
            return (results, statistical_result) if quantity > 1 else (results[0], statistical_result)

        return results if quantity > 1 else results[0]

    def calculate_statistic(self, values, operation):
        """Calculates a statistic (mean or sum) from the extracted numerical values."""
        numbers = [value for value in values if isinstance(value, (int, float))]
        if operation == 'mean':
            return sum(numbers) / len(numbers) if numbers else 0
        elif operation == 'sum':
            return sum(numbers)
        else:
            raise ValueError(f"Unsupported operation: {operation}")

    def extract_numerical_values(self, data):
        """Extracts numerical values recursively from the data."""
        numerical_values = []
        if isinstance(data, dict):
            for value in data.values():
                numerical_values.extend(self.extract_numerical_values(value))
        elif isinstance(data, list) or isinstance(data, tuple):
            for item in data:
                numerical_values.extend(self.extract_numerical_values(item))
        elif isinstance(data, (int, float)):
            numerical_values.append(data)
        return numerical_values

# Creating an instance of DataProcessor
data_processor = DataProcessor()

# Defining data structures
student = {
    'name': data_processor.faker.name(),
    'age': random.randint(16, 25),
    'math_score': round(random.uniform(60, 100), 2),
    'gender': random.choice(['Male', 'Female']),
}

teacher = {
    'name': data_processor.faker.name(),
    'age': random.randint(25, 45),
    'major': random.choice(['math', 'english', 'chinese']),
    'gender': random.choice(['Male', 'Female']),
}

# Generating data and calculating the sum of all numerical nodes in a dictionary
dict_output, sum_total = data_processor.generate(1, 'dict', operation='sum', student=student, teacher=teacher)
print("Generated dictionary:", dict_output)
print("Sum of numerical nodes:", sum_total)

# Generating multiple lists and calculating the mean of all numerical nodes
list_outputs, mean_values = data_processor.generate(3, 'list', operation='mean', a=1, b={'hello': [3, 4]})
print("\nGenerated lists:", list_outputs)
print("Mean of numerical nodes:", mean_values)
