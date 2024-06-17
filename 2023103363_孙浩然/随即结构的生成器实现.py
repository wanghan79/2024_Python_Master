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
def generate_school_structure(schools):
    """生成学校部门结构的函数"""
    school_structure = {}
    for school in schools:
        teachers = random.randint(10, 100)
        papers = [f"项目{random.randint(1, 10)}"] * random.randint(1, 5)
        school_structure[school] = {
            "学校名称": school,
            "教师数量": teachers,
            "论文列表": papers
        }
    return school_structure

# 测试
school = ["985", "211", "普通本科", "专科"]
generate_school_structure(school)
