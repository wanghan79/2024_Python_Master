import random
import string

def generate_random_value(value_template, **kwargs):
    """根据输入值的类型生成随机值，并根据额外的 kwargs 自定义生成规则。"""
    value_type = type(value_template)
    if value_type is str:
        # 生成一个长度在 min_length 和 max_length 之间的随机字符串
        min_length = kwargs.get('min_length', 5)
        max_length = kwargs.get('max_length', 10)
        length = random.randint(min_length, max_length)
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
    elif value_type is int:
        # 生成一个介于 min_value 和 max_value 之间的随机整数
        min_value = kwargs.get('min_value', 1)
        max_value = kwargs.get('max_value', 100)
        return random.randint(min_value, max_value)
    elif value_type is float:
        # 生成一个介于 min_value 和 max_value 之间的随机浮点数，并保留两位小数
        min_value = kwargs.get('min_value', 0.0)
        max_value = kwargs.get('max_value', 100.0)
        return round(random.uniform(min_value, max_value), 2)
    elif value_type is list:
        # 生成一个列表，列表中的每个项都是根据模板列表中的项生成的随机值
        min_length = kwargs.get('min_length', len(value_template) // 2)
        max_length = kwargs.get('max_length', len(value_template))
        length = random.randint(min_length, max_length)
        return [generate_random_value(item, **kwargs) for item in value_template[:length]]
    elif value_type is tuple:
        # 生成一个元组，元组中的每个项都是根据模板元组中的项生成的随机值
        return tuple(generate_random_value(item, **kwargs) for item in value_template)
    elif value_type is dict:
        # 生成一个字典，字典中的每一项键值对都是根据模板字典中的项生成的随机值
        return {key: generate_random_value(value, **kwargs) for key, value in value_template.items()}
    else:
        # 对于不支持的类型，返回 None
        return None


student_template = {
    "name": "Jack",
    "age": 20=3,
    "major": "Computer Science",
    "gpa": 4.0,
    "courses": ["Math","Data Structures"],
    "contact": {
        "email": "Jack@example.com",
        "phone": "123-456-7890"
    }
}

# 使用自定义的 kwargs 生成随机学生档案
random_student_profiles = [
    generate_random_value(profile, min_length=3, max_length=12, min_value=18, max_value=30)
    for profile in [student_template] * 5  # 生成5个档案
]

for profile in random_student_profiles:
    print(profile)