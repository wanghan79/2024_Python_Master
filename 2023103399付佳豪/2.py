from faker import Faker
import random

fake_generator = Faker()

class ContentGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_content(self, quantity, datatype, computation=None, **content):
        if datatype not in ['string', 'list', 'dict', 'tuple']:
            raise ValueError(f"不支持的数据类型: {datatype}")

        def parse_recursively(element):
            if isinstance(element, dict):
                return {key: parse_recursively(value) for key, value in element.items()}
            elif isinstance(element, list):
                return [parse_recursively(item) for item in element]
            elif isinstance(element, tuple):
                return tuple(parse_recursively(item) for item in element)
            else:
                return element

        results = []
        numeric_values = []

        for _ in range(quantity):
            structured_data = parse_recursively(content)
            if datatype == 'string':
                outcome = ''.join(map(str, structured_data.values()))
            elif datatype == 'list':
                outcome = list(structured_data.values())
            elif datatype == 'dict':
                outcome = structured_data
            elif datatype == 'tuple':
                outcome = tuple(structured_data.values())

            results.append(outcome)
            numeric_values.extend(self.extract_numbers(structured_data))

        if computation:
            statistical_result = self.perform_calculation(numeric_values, computation)
            return results if quantity > 1 else results[0], statistical_result

        return results if quantity > 1 else results[0]

    def perform_calculation(self, values, operation):
        numbers = [num for num in values if isinstance(num, (int, float))]

        if operation == 'mean':
            return sum(numbers) / len(numbers) if numbers else 0
        elif operation == 'sum':
            return sum(numbers)
        else:
            raise ValueError(f"不支持的操作: {operation}")

    def extract_numbers(self, data):
        collected_numbers = []
        if isinstance(data, dict):
            for value in data.values():
                collected_numbers.extend(self.extract_numbers(value))
        elif isinstance(data, list) or isinstance(data, tuple):
            for item in data:
                collected_numbers.extend(self.extract_numbers(item))
        elif isinstance(data, (int, float)):
            collected_numbers.append(data)
        return collected_numbers


# 实例化类
data_creator = ContentGenerator()

# 定义数据结构
pupil = {
    'name': fake_generator.name(),
    'age': random.randint(16, 25),
    'math_score': round(random.uniform(60, 100), 2),
    'gender': random.choice(['Male', 'Female']),
}

educator = {
    'name': fake_generator.name(),
    'age': random.randint(25, 45),
    'major': random.choice(['math', 'english', 'chinese']),
    'gender': random.choice(['Male', 'Female']),
}

# 生成字典并计算所有数值节点的总和
generated_dict, total_of_numbers = data_creator.generate_content(1, 'dict', computation='sum', key1=pupil, key2=educator)
print("生成的字典:", generated_dict)
print("数值节点的总和:", total_of_numbers)

# 生成多个列表并计算所有数值节点的均值
list_of_results, average_of_values = data_creator.generate_content(3, 'list', computation='mean', item1=1, item2={'hello': [3, 4]})
print("\n生成的列表:", list_of_results)
print("数值节点的均值:", average_of_values)
