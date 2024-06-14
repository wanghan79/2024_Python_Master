import random
import string

# 作业1 ： 随机生成指定数据结构的函数 使用递归进行生成 4组测试样例进行测试

# 1.产生随机整数
def generate_random_number(low=0, high=100):
    return random.randint(low, high)
# 2.产生随机字符串
def generate_random_string(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

# 3.递归产生随机结构 包括字典 列表 元组 整型 字符串 以及嵌套循环结构
def generate_random_structure(structure):
    if isinstance(structure, dict):
        return {key: generate_random_structure(value) for key, value in structure.items()}
    elif isinstance(structure, list):
        return [generate_random_structure(element) for element in structure]
    elif isinstance(structure, tuple) and len(structure) == 2 and structure[0] == 'list':
        return [generate_random_structure(structure[1]) for _ in range(generate_random_number(1, 5))]
    elif structure == 'int':
        return generate_random_number()
    elif structure == 'string':
        return generate_random_string()
    else:
        return structure

# 4.随机生成函数 如果没有指定生成随机结构的数量 count 则默认为1
def random_data_generator(structure, *args, **kwargs):
    count = kwargs.get('count', 1)
    return [generate_random_structure(structure) for _ in range(count)]

# 5.4个测试样例

# 6.Example 1: 生成包含学生信息的结构，其中嵌套了地址信息。生成5个随机学生数据。


student_structure = {
    'name': 'string',
    'student_id': 'int',
    'major': 'string',
    'direction': 'string',
    'address': {
        'street': 'string',
        'city': 'string',
        'zip_code': 'int'
    }
}

random_students = random_data_generator(student_structure, count=5)
print("Example 1: 包含嵌套地址的学生结构")
for student in random_students:
    print(student)

# 7.Example 2: 生成项目组信息，其中每个项目组包含一个随机长度的成员列表。生成5个随机项目组数据。
project_structure = {
    'project_name': 'string',
    'project_id': 'int',
    'members': ('list', {
        'member_name': 'string',
        'member_id': 'int',
        'role': 'string'
    })
}

random_projects = random_data_generator(project_structure, count=5)
print("\nExample 2: 随机项目组")
for project in random_projects:
    print(project)

# 8.Example 3: : 生成公司信息，其中每个公司包含多个部门信息，每个部门包含多个员工信息。生成2个随机公司数据。
company_structure = {
    'company_name': 'string',
    'company_id': 'int',
    'departments': ('list', {
        'department_name': 'string',
        'department_id': 'int',
        'employees': ('list', {
            'employee_name': 'string',
            'employee_id': 'int',
            'position': 'string'
        })
    })
}

random_companies = random_data_generator(company_structure, count=2)
print("\nExample 3: 随机的公司部门员工信息")
for company in random_companies:
    print(company)

# 9.Example 4: 生成商品信息，其中每个商品包含多个评论信息。生成3个随机商品数据。
product_structure = {
    'product_name': 'string',
    'product_id': 'int',
    'price': 'int',
    'category': 'string',
    'reviews': ('list', {
        'review_id': 'int',
        'review_text': 'string',
        'rating': 'int'
    })
}

random_products = random_data_generator(product_structure, count=3)
print("\nExample 4: 随机商品信息")
for product in random_products:
    print(product)