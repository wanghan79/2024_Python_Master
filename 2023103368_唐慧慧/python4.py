import random
from functools import wraps

def random_structure_decorator(func):
    """随机结构生成器的修饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"生成的随机结构：{result}")
        return result
    return wrapper

@random_structure_decorator
def generate_student_grades(students):
    """生成学生课程成绩的函数"""
    courses = ["数学", "英语", "物理", "化学", "历史"]
    student_grades = {}
    for student in students:
        grades = {course: random.randint(60, 100) for course in courses}
        student_grades[student] = {
            "学生姓名": student,
            "课程成绩": grades
        }
    return student_grades

# 测试
students = ["张三", "李四", "王五", "赵六"]
generate_student_grades(students)
