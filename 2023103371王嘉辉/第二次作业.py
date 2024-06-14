from faker import Faker
import random

class FakeDataCreator:
    def __init__(self, seed=None):
        self.fake = Faker()
        if seed is not None:
            random.seed(seed)

    def create_data(self, count, data_structure, data_type, operation=None):
        if data_type not in ['string', 'list', 'dict', 'tuple']:
            raise ValueError(f"Unsupported data type: {data_type}")

        def parse_data_structure(data_structure):
            if isinstance(data_structure, dict):
                return {key: self.fake.text() for key in data_structure}
            elif isinstance(data_structure, list):
                return [self.fake.text() for _ in data_structure]
            else:
                return self.fake.text()

        data = []
        numeric_values = []

        for _ in range(count):
            if data_structure:
                structured_data = parse_data_structure(data_structure)
            else:
                structured_data = self.fake.text()

            if data_type == 'string':
                data.append(''.join(map(str, structured_data)))
            elif data_type == 'list':
                data.append(list(structured_data))
            elif data_type == 'dict':
                data.append(structured_data)
            elif data_type == 'tuple':
                data.append(tuple(structured_data))

            numeric_values.extend(self._extract_numeric(structured_data))

        if operation:
            result = getattr(self, f'_calculate_{operation}')(numeric_values)
            return data if count > 1 else data[0], result

        return data if count > 1 else data[0]

    def _extract_numeric(self, data):
        numeric_values = []
        if isinstance(data, dict):
            for value in data.values():
                numeric_values.extend(self._extract_numeric(value))
        elif isinstance(data, list) or isinstance(data, tuple):
            for item in data:
                numeric_values.extend(self._extract_numeric(item))
        elif isinstance(data, (int, float)):
            numeric_values.append(data)
        return numeric_values

    def _calculate_mean(self, data):
        return sum(data) / len(data) if data else 0

    def _calculate_sum(self, data):
        return sum(data)

if __name__ == "__main__":
    creator = FakeDataCreator(seed=42)

    student_structure = ['name', 'age', 'math_score', 'gender']
    teacher_structure = ['name', 'age', 'major', 'gender']

    result_dict, total_sum = creator.create_data(1, data_structure=None, data_type='dict', operation='sum')
    print("生成的字典:", result_dict)
    print("数字节点的总和:", total_sum)

    result_lists, mean_value_lists = creator.create_data(3, data_structure=None, data_type='list', operation='mean')
    print("\n生成的列表:", result_lists)
    print("数字节点的均值:", mean_value_lists)
