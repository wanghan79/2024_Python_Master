import random
import string
import numpy as np

# 作业4 随机结构的生成器模式

# 随机数据生成器类
class RandomDataGenerator:
    def generate_random_number(self, low=0, high=100):
        return random.randint(low, high)

    def generate_random_float(self, low=0.0, high=100.0):
        return random.uniform(low, high)

    def generate_random_string(self, length=10):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    def generate_random_boolean(self):
        return random.choice([True, False])

# 生成器模式的生成器类
class DataBuilder:
    def __init__(self):
        self.data = None
        self.generator = RandomDataGenerator()

    def reset(self):
        self.data = None

    def build_int(self, low=0, high=100):
        self.data = self.generator.generate_random_number(low, high)
        return self

    def build_float(self, low=0.0, high=100.0):
        self.data = self.generator.generate_random_float(low, high)
        return self

    def build_string(self, length=10):
        self.data = self.generator.generate_random_string(length)
        return self

    def build_boolean(self):
        self.data = self.generator.generate_random_boolean()
        return self

    def build_list(self, element_type, size=None):
        size = size or self.generator.generate_random_number(1, 5)
        self.data = [element_type() for _ in range(size)]
        return self

    def build_dict(self, structure):
        self.data = {key: value() for key, value in structure.items()}
        return self

    def get_data(self):
        return self.data

# Director类 指导生成器如何一步步构建对象
class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct(self, structure):
        if isinstance(structure, dict):
            return self._builder.build_dict({key: lambda s=structure[key]: self.construct(s) for key in structure}).get_data()
        elif isinstance(structure, list):
            return self._builder.build_list(lambda s=structure[0]: self.construct(s)).get_data()
        elif isinstance(structure, tuple) and len(structure) == 2:
            if structure[0] == 'list':
                return self._builder.build_list(lambda s=structure[1]: self.construct(s)).get_data()
            elif structure[0] == 'range':
                return self._builder.build_int(structure[1][0], structure[1][1]).get_data()
            elif structure[0] == 'float_range':
                return self._builder.build_float(structure[1][0], structure[1][1]).get_data()
        elif structure == 'int':
            return self._builder.build_int().get_data()
        elif structure == 'float':
            return self._builder.build_float().get_data()
        elif structure == 'string':
            return self._builder.build_string().get_data()
        elif structure == 'bool':
            return self._builder.build_boolean().get_data()
        else:
            return structure

# 统计功能修饰器，接收要统计的字段参数
def statistics_decorator(numeric_fields, *operations):
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            results = {}
            for field in numeric_fields:
                flat_data = flatten_data(data, field)
                field_results = {}
                for operation in operations:
                    if operation == 'sum':
                        field_results['sum'] = np.sum(flat_data)
                    elif operation == 'mean':
                        field_results['mean'] = np.mean(flat_data)
                    elif operation == 'variance':
                        field_results['variance'] = np.var(flat_data)
                results[field] = field_results
            return data, results
        return wrapper
    return decorator

# 帮助函数，将嵌套的数据结构平铺成数值列表
def flatten_data(data, field):
    keys = field.split('.')

    def get_nested_values(d, keys):
        if not keys:
            return [d] if isinstance(d, (int, float)) else []
        key = keys[0]
        rest_keys = keys[1:]
        if isinstance(d, list):
            values = []
            for item in d:
                values.extend(get_nested_values(item, rest_keys))
            return values
        elif isinstance(d, dict):
            if key in d:
                return get_nested_values(d[key], rest_keys)
            else:
                return []
        else:
            return []

    flat_data = []
    for item in data:
        flat_data.extend(get_nested_values(item, keys))

    return flat_data

# 生成学生数据的函数，使用统计修饰器
@statistics_decorator(['score'], 'sum', 'mean', 'variance')
def generate_student_data(count):
    builder = DataBuilder()
    director = Director(builder)
    student_structure = {
        'name': 'string',
        'student_id': 'int',
        'major': 'string',
        'direction': 'string',
        'score': 'int',
        'address': {
            'street': 'string',
            'city': 'string',
            'zip_code': 'int'
        }
    }
    return [director.construct(student_structure) for _ in range(count)]

# 测试样例：生成员工数据的函数，使用统计修饰器
@statistics_decorator(['salary'], 'sum', 'mean', 'variance')
def generate_employee_data(count):
    builder = DataBuilder()
    director = Director(builder)
    employee_structure = {
        'name': 'string',
        'employee_id': 'int',
        'department': 'string',
        'position': 'string',
        'salary': ('float_range', (3000.0, 15000.0))
    }
    return [director.construct(employee_structure) for _ in range(count)]

# 示例用法
if __name__ == "__main__":
    # 生成5个学生数据，并计算统计信息
    student_data, student_stats = generate_student_data(5)
    print("生成的学生数据示例（前5个）：")
    for student in student_data[:5]:
        print(student)
    print("\n生成的学生得分统计信息：")
    print(student_stats)

    # 生成5个员工数据，并计算统计信息
    employee_data, employee_stats = generate_employee_data(5)
    print("\n生成的员工数据示例（前5个）：")
    for employee in employee_data[:5]:
        print(employee)
    print("\n生成的员工薪水统计信息：")
    print(employee_stats)
