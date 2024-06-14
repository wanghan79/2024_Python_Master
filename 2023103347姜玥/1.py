import random
import string

data = {
    '基本信息': {
        '姓名': 3,
        '年龄': (17, 30),
        '学号': 7,
        '身高': (155, 190)
    },
    '联系方式': {
        '电话': 11,
        'email': 5
    },
    '成绩': {
        '语文': (60, 100),
        '数学': (60, 100),
        '英语': (60, 100)
    }
}

def generate_random_name(length=3):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate_random_age(min_age=17, max_age=30):
    return random.randint(min_age, max_age)

def generate_random_student_id(length=7):
    return ''.join(random.choice('0123456789') for _ in range(length))

def generate_random_height(min_height=155, max_height=190):
    return random.randint(min_height, max_height)

def generate_random_phone_number(length=11):
    return ''.join(random.choice('0123456789') for _ in range(length))

def generate_random_email(length=5):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length)) + '@example.com'

def generate_random_score(min_score=60, max_score=100):
    return random.randint(min_score, max_score)

def generate_random_info(data):
    if isinstance(data, int):  # 基本数据类型，直接生成
        return generate_random_name(data)
    elif isinstance(data, tuple):  # 年龄身高
        return generate_random_age(*data)
    elif isinstance(data, dict):  # 嵌套字典，递归生成
        return {key: generate_random_info(value) for key, value in data.items()}
    else:
        raise ValueError("Unsupported data type")

def generate_students_info(data_structure, count):
    return [generate_random_info(data_structure) for _ in range(count)]

# 指定生成的学生数量
student_count = 5  # 生成5个学生信息
students = generate_students_info(data, student_count)

# 打印学生信息
for student in students:
    print(f"姓名: {student['基本信息']['姓名']}, 年龄: {student['基本信息']['年龄']}岁, "
          f"学号: {student['基本信息']['学号']}, 身高: {student['基本信息']['身高']}厘米, "
          f"电话: {student['联系方式']['电话']}, email: {student['联系方式']['email']}, "
          f"语文成绩: {student['成绩']['语文']}, 数学成绩: {student['成绩']['数学']}, "
          f"英语成绩: {student['成绩']['英语']}")