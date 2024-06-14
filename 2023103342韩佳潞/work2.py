import random
import string

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

def main():
    students = [create_student(data_type['field_types']) for _ in range(data_type['num_students'])]

    for student in students:
        print(student)

main()
