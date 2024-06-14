import random
import string
import numpy as np

# 作业3 在封装类的基础上添加修饰器进行数据统计功能

# 随机数据生成器类
class RandomDataGenerator:
    def __init__(self):
        pass

    # 生成随机整数
    def generate_random_number(self, low=0, high=100):
        return random.randint(low, high)

    # 生成随机字符串
    def generate_random_string(self, length=10):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    # 生成随机结构数据
    def generate_random_structure(self, structure):
        if isinstance(structure, dict):
            return {key: self.generate_random_structure(value) for key, value in structure.items()}
        elif isinstance(structure, list):
            return [self.generate_random_structure(element) for element in structure]
        elif isinstance(structure, tuple) and len(structure) == 2 and structure[0] == 'list':
            return [self.generate_random_structure(structure[1]) for _ in range(self.generate_random_number(1, 5))]
        elif structure == 'int':
            return self.generate_random_number()
        elif structure == 'string':
            return self.generate_random_string()
        else:
            return structure

    # 主生成函数，根据指定结构生成指定数量的数据
    def generate(self, structure, count=1):
        return [self.generate_random_structure(structure) for _ in range(count)]


# 统计功能修饰器，接收要统计的字段参数
def statistics_decorator(numeric_fields, *operations):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 调用被修饰函数生成数据
            data = func(*args, **kwargs)
            # 分别平铺数据，专门统计指定字段
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
                    # 可以添加更多的统计操作
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
    generator = RandomDataGenerator()
    student_structure = {
        'name': 'string',
        'student_id': 'int',
        'major': 'string',
        'direction': 'string',
        'score': 'int',  # 添加学生得分字段
        'address': {
            'street': 'string',
            'city': 'string',
            'zip_code': 'int'
        }
    }
    return generator.generate(student_structure, count=count)


# 新的测试样例：生成员工数据的函数，使用统计修饰器
@statistics_decorator(['salary'], 'sum', 'mean', 'variance')
def generate_employee_data(count):
    generator = RandomDataGenerator()
    employee_structure = {
        'name': 'string',
        'employee_id': 'int',
        'department': 'string',
        'position': 'string',
        'salary': 'int'  # 添加员工薪水字段
    }
    return generator.generate(employee_structure, count=count)


# 示例用法
if __name__ == "__main__":
    # 生成指定数量个学生数据，并计算统计信息，这里我们以5为测试
    student_data, student_stats = generate_student_data(5)

    # 显示生成的学生数据和统计信息
    print("生成的学生数据示例（前5个）：")
    for student in student_data[:5]:  # 只显示前5个学生数据
        print(student)

    print("\n生成的学生得分统计信息：")
    print(student_stats)

    # 生成5个员工数据，并计算统计信息
    employee_data, employee_stats = generate_employee_data(5)

    # 显示生成的员工数据和统计信息
    print("\n生成的员工数据示例（前5个）：")
    for employee in employee_data[:5]:  # 只显示前5个员工数据
        print(employee)

    print("\n生成的员工薪水统计信息：")
    print(employee_stats)
