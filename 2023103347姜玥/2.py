import random
import string

class RandomDataGenerator:
    def __init__(self):
        pass

    def generate_random_string(self, length):
        """生成指定长度的随机字符串，只包含小写字母。"""
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    def generate_random_number(self, length):
        """生成指定长度的随机数字字符串。"""
        return ''.join(random.choice('0123456789') for _ in range(length))

    def generate_random_age(self, min_age, max_age):
        """生成指定范围的随机年龄。"""
        return random.randint(min_age, max_age)

    def generate_random_score(self, min_score, max_score):
        """生成指定范围的随机分数。"""
        return random.randint(min_score, max_score)

    def generate_random_info(self, data):
        """递归生成随机数据。"""
        if isinstance(data, int):
            return self.generate_random_string(data)
        elif isinstance(data, tuple) and len(data) == 2:
            return self.generate_random_age(data[0], data[1])
        elif isinstance(data, dict):
            return {key: self.generate_random_info(value) for key, value in data.items()}
        else:
            raise ValueError("Unsupported data type")

    def generate_students_info(self, data_structure, count):
        """根据数据结构和数量生成学生信息列表。"""
        return [self.generate_random_info(data_structure) for _ in range(count)]

data_structure = {
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

generator = RandomDataGenerator()
student_count = 5  # 生成的学生数量
students_info = generator.generate_students_info(data_structure, student_count)

# 打印学生信息
for student in students_info:
    print(f"学生信息 - 姓名: {student['基本信息']['姓名']}, 年龄: {student['基本信息']['年龄']}, "
          f"学号: {student['基本信息']['学号']}, 身高: {student['基本信息']['身高']}, "
          f"电话: {student['联系方式']['电话']}, Email: {student['联系方式']['email']}, "
          f"语文成绩: {student['成绩']['语文']}, 数学成绩: {student['成绩']['数学']}, "
          f"英语成绩: {student['成绩']['英语']}")