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
def generate_company_structure(departments):
    """生成公司部门结构的函数"""
    company_structure = {}
    for department in departments:
        employees = random.randint(10, 100)
        projects = [f"项目{random.randint(1, 10)}"] * random.randint(1, 5)
        company_structure[department] = {
            "部门名称": department,
            "员工数量": employees,
            "项目列表": projects
        }
    return company_structure

# 测试
departments = ["研发部", "市场部", "财务部", "人力资源部"]
generate_company_structure(departments)
