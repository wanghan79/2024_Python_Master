import random
import string
import time

class Student:
    def __init__(self, name, student_id, major, grades, research):
        self.name = name
        self.student_id = student_id
        self.major = major
        self.grades = grades
        self.research = research

    def __str__(self):
        return f"姓名：{self.name}, 学号：{self.student_id}, 专业：{self.major}, 成绩：{self.grades}, 课程：{self.research}"

def create_string(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def create_int(max_value=100):
    return random.randint(1, max_value)

def create_list(element_type, length=5):
    if element_type == 'int':
        return [create_int() for _ in range(length)]
    elif element_type == 'string':
        return [create_string() for _ in range(length)]
    else:
        raise ValueError("不属于list")

def create_tuple(element_type, length=5):
    return tuple(create_list(element_type, length))

# def select_types():
#     fields = ['name', 'student_id', 'major', 'grades', 'research']
#     field_types = {}
#     for field in fields:
#         field_type = input(f"输入{field}数据类型(string, int, list, tuple): ")
#         if field_type == 'list' or field_type == 'tuple':
#             element_type = input(f"输入{field_type} 中 {field} 类型(int or string): ")
#             field_types[field] = (field_type, element_type)
#         else:
#             field_types[field] = (field_type, None)
#     return field_types

# def create_student(field_types):
#     data = {}
#     for field, (field_type, element_type) in field_types.items():
#         if field_type == 'string':
#             data[field] = create_string()
#         elif field_type == 'int':
#             data[field] = create_int()
#         elif field_type == 'list':
#             data[field] = create_list(element_type)
#         elif field_type == 'tuple':
#             data[field] = create_tuple(element_type)
#         else:
#             raise ValueError("类型输入错误")
#     return Student(**data)

def create_student(field_types):
    data = {}
    for field, (field_type, element_type, length) in field_types.items():
        if field_type == 'string':
            data[field] = create_string(length)
        elif field_type == 'int':
            data[field] = create_int()
        elif field_type == 'list':
            data[field] = create_list(element_type, length)
        elif field_type == 'tuple':
            data[field] = create_tuple(element_type, length)
        else:
            raise ValueError("类型输入错误")
    return Student(**data)


#修饰器
def log_function_data(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"调用 {func.__name__}，参数为：args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 执行完成，耗时 {end_time - start_time:.2f} 秒")
        return result
    return wrapper

@log_function_data
def process_data(*args):
    if not args:
        print("没有提供数据")
        return

    operations = []
    data = []

    for arg in args:
        if isinstance(arg, str) and arg.lower() in ['sum', 'mean']:
            operations.append(arg.lower())
        elif isinstance(arg, list):    #分数
            data.append(arg)

    results = {}
    if operations:
        if 'sum' in operations:
            results['sum'] = sum(data[0])
        if 'mean' in operations:
            results['mean'] = sum(data[0]) / len(data[0]) if data[0] else 0
    else:
        print("什么都不求")
        return

    for key, value in results.items():
        print(f"{key.capitalize()}: {value}")



data_type = {
    'num_students': 3,
    'field_types': {
        'name': ('string', None, 10),
        'student_id': ('string', None, 10),
        'major': ('string', None, 8),
        'grades': ('list', 'int', 5),
        'research': ('tuple', 'string', 3)
    }
}

def main():
    students = [create_student(data_type['field_types']) for _ in range(data_type['num_students'])]

    for student in students:
        print(student)

        print("sum and mean:")
        process_data('sum', 'mean', student.grades)
        print("sum only:")
        process_data('sum', student.grades)
        print("mean only:")
        process_data('mean', student.grades)
        print("not all:")
        process_data(student.grades)

main()