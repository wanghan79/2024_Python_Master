from faker import Faker
import random

fake = Faker()

class DataGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_data(self, count, datetype, operation=None, **kwargs):
        if datetype not in ['string', 'list', 'dict', 'tuple']:
            raise ValueError(f"Unsupported data type: {datetype}")

        def recursive_parse(data):
            if isinstance(data, dict):
                return {key: recursive_parse(value) for key, value in data.items()}
            elif isinstance(data, list):
                return [recursive_parse(item) for item in data]
            elif isinstance(data, tuple):
                return tuple(recursive_parse(item) for item in data)
            else:
                return data

        results = []
        numeric_data = []

        for _ in range(count):
            parsed_data = recursive_parse(kwargs)
            if datetype == 'string':
                result = ''.join(map(str, parsed_data.values()))
            elif datetype == 'list':
                result = list(parsed_data.values())
            elif datetype == 'dict':
                result = parsed_data
            elif datetype == 'tuple':
                result = tuple(parsed_data.values())

            results.append(result)
            numeric_data.extend(self._extract_numeric(parsed_data))

        if operation:
            statistic = self.calculate(numeric_data, operation)
            return results if count > 1 else results[0], statistic

        return results if count > 1 else results[0]

    def calculate(self, data, operation):
        numeric_data = [x for x in data if isinstance(x, (int, float))]

        if operation == 'mean':
            return sum(numeric_data) / len(numeric_data) if numeric_data else 0
        elif operation == 'sum':
            return sum(numeric_data)
        else:
            raise ValueError(f"Unsupported operation: {operation}")

    def _extract_numeric(self, data):
        numeric_data = []
        if isinstance(data, dict):
            for value in data.values():
                numeric_data.extend(self._extract_numeric(value))
        elif isinstance(data, list) or isinstance(data, tuple):
            for item in data:
                numeric_data.extend(self._extract_numeric(item))
        elif isinstance(data, (int, float)):
            numeric_data.append(data)
        return numeric_data


# 实例化类
generator = DataGenerator()

# 定义数据结构
student = {
    'name': fake.name(),
    'age': random.randint(16, 25),  # 假设年龄在16到25岁之间
    'math_score': round(random.uniform(60, 100), 2),  # 数学成绩在60到100分之间，保留两位小数
    'gender': random.choice(['Male', 'Female']),  # 随机性别
}

teacher = {
    'name': fake.name(),
    'age': random.randint(25, 45),  # 假设年龄在25到45岁之间
    'major': random.choice(['math', 'english', 'chinese']),  # 随机专业
    'gender': random.choice(['Male', 'Female']),  # 随机性别
}

# 生成一个字典并计算所有数字节点的总和
result_dict, total_sum = generator.generate_data(1, 'dict', operation='sum', key1=student, key2=teacher)
print("生成的字典:", result_dict)
print("数字节点的总和:", total_sum)

# 生成多个列表并计算所有数字节点的均值
result_lists, mean_value_lists = generator.generate_data(3, 'list', operation='mean', a=1, b={'hello': [3, 4]})
print("\n生成的列表:", result_lists)
print("数字节点的均值:", mean_value_lists)