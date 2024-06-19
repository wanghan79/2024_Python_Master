import random
import string
import datetime


def generate_random_value(value_type):
    if isinstance(value_type, tuple):
        base_type = value_type[0]
        if base_type == 'int':
            return random.randint(*value_type[1:])
        elif base_type == 'str':
            length = random.randint(*value_type[1:]) if len(value_type) > 1 else 10
            return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        elif base_type == 'float':
            return random.uniform(*value_type[1:])
        elif base_type == 'bool':
            return random.choice([True, False])
        elif base_type == 'datetime':
            start, end = value_type[1:]
            return start + datetime.timedelta(
                seconds=random.randint(0, int((end - start).total_seconds()))
            )
        elif callable(base_type):
            return base_type(*value_type[1:])
    elif value_type == 'int':
        return random.randint(0, 100)
    elif value_type == 'str':
        return ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    elif value_type == 'float':
        return random.uniform(0.0, 100.0)
    elif value_type == 'bool':
        return random.choice([True, False])
    elif value_type == 'datetime':
        return datetime.datetime.now()
    else:
        return None


def generate_random_structure(struct):
    if isinstance(struct, dict):
        return {k: generate_random_structure(v) for k, v in struct.items()}
    elif isinstance(struct, list):
        return [generate_random_structure(struct[0]) for _ in range(len(struct))]
    elif isinstance(struct, tuple):
        return tuple(generate_random_structure(struct[0]) for _ in range(len(struct)))
    else:
        return generate_random_value(struct)


def generate_random_data(structure, size=1):
    return [generate_random_structure(structure) for _ in range(size)]


structure = {
    "name": ("str", 5, 15),
    "student_id": ("int", 1000, 9999),
    "major": "str",
    "advisor": "str",
    "contact": ("str", 10, 20),
    "target_company": "str",
    "research_area": "str",
    "enrollment_date": ("datetime", datetime.datetime(2010, 1, 1), datetime.datetime(2020, 12, 31))
}

random_students = generate_random_data(structure, size=1000)
print(random_students[:5])  # 打印前五个生成的随机信息
