import random
import string
from faker import Faker

# 初始化Faker库，用于生成真实的假数据
fake = Faker()

# 生成指定长度的随机字符串
def generate_random_string(length=10):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

# 根据输入的结构递归生成随机数据
def generate_random_data_from_structure(structure):
    """根据输入的类型和结构递归生成随机数据。"""
    if isinstance(structure, int):
        return random.randint(0, 100)
    elif isinstance(structure, float):
        return random.uniform(0, 10000)
    elif isinstance(structure, str):
        return generate_random_string(len(structure))
    elif isinstance(structure, list):
        return [generate_random_data_from_structure(item) for item in structure]
    elif isinstance(structure, tuple):
        return tuple(generate_random_data_from_structure(item) for item in structure)
    elif isinstance(structure, dict):
        return {key: generate_random_data_from_structure(value) for key, value in structure.items()}
    else:
        return None

# 根据模板生成多个随机数据记录的生成器
def generate_random_records(template, record_count):
    """根据提供的模板生成多个随机数据记录。"""
    for _ in range(record_count):
        yield generate_random_data_from_structure(template)

# 定义一个样本数据结构模板
sample_data_structure = {
    "姓名": fake.name(),
    "年龄": 18,
    "考试成绩": [10, 20, 30],
    "联系信息": {
        "城市": "长春",
        "邮箱": "Alen@example.com"
    },
    "专业": "计算机科学"
}

# 根据样本结构生成并打印10个随机数据记录
print("根据样本结构生成10个随机数据记录：")
for record in generate_random_records(sample_data_structure, 10):
    print(record)