from faker import Faker
import random

fake = Faker()

class DataGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_data(self, count, data_type, operation=None, **kwargs):
        if data_type not in ['string', 'list', 'dict', 'tuple']:
            raise ValueError(f"Unsupported data type: {data_type}")

        def recursive_parse(data):
            if isinstance(data, dict):
                return {key: recursive_parse(value) for key, value in data.items()}
            elif isinstance(data, list) or isinstance(data, tuple):
                return type(data)(recursive_parse(item) for item in data)
            else:
                return data

        results = []
        numeric_data = []

        for _ in range(count):
            parsed_data = recursive_parse(kwargs)
            if data_type == 'string':
                result = ''.join(map(str, parsed_data.values()))
            elif data_type == 'list':
                result = list(parsed_data.values())
            elif data_type == 'dict':
                result = parsed_data
            elif data_type == 'tuple':
                result = tuple(parsed_data.values())

            results.append(result)
            numeric_data.extend(self._extract_numeric(parsed_data))

        if operation:
            statistic = self.calculate(numeric_data, operation)
            return (results, statistic) if count > 1 else (results[0], statistic)

        return (results, None) if count > 1 else (results[0], None)

    def calculate(self, data, operation):
        numeric_data = [x for x in data if isinstance(x, (int, float))]

        if operation == 'mean':
            return sum(numeric_data) / len(numeric_data) if numeric_data else 0
        elif operation == 'sum':
            return sum(numeric_data)
        else:
            raise ValueError(f"Unsupported operation: {operation}")

    def _extract_numeric(self, data):
        if isinstance(data, dict):
            return [val for value in data.values() for val in self._extract_numeric(value)]
        elif isinstance(data, list) or isinstance(data, tuple):
            return [val for item in data for val in self._extract_numeric(item)]
        elif isinstance(data, (int, float)):
            return [data]
        return []

# 实例化类
generator = DataGenerator()

# 定义数据结构
student = {
    'name': fake.name(),
    'age': random.randint(16, 25),
    'math_score': round(random.uniform(60, 100), 2),
    'gender': random.choice(['Male', 'Female']),
}

teacher = {
    'name': fake.name(),
    'age': random.randint(25, 45),
    'major': random.choice(['math', 'english', 'chinese']),
    'gender': random.choice(['Male', 'Female']),
}

# 生成一个字典并计算所有数字节点的总和
result_dict, total_sum = generator.generate_data(1, 'dict', operation='sum', student=student, teacher=teacher)
print("生成的字典:", result_dict)
print("数字节点的总和:", total_sum)

# 生成多个列表并计算所有数字节点的均值
result_lists, mean_value_lists = generator.generate_data(3, 'list', operation='mean', a=1, b={'hello': [3, 4]})
print("\n生成的列表:", result_lists)
print("数字节点的均值:", mean_value_lists)
