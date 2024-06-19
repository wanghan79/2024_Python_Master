import random
import string
import datetime


class RandomDataGenerator:
    @staticmethod
    def generate_data(structure, size=1):
        def generate_value(value_type):
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

        def generate_structure(struct):
            if isinstance(struct, dict):
                return {k: generate_structure(v) for k, v in struct.items()}
            elif isinstance(struct, list):
                return [generate_structure(struct[0]) for _ in range(len(struct))]
            elif isinstance(struct, tuple):
                return tuple(generate_structure(struct[0]) for _ in range(len(struct)))
            else:
                return generate_value(struct)

        for _ in range(size):
            yield generate_structure(structure)

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

generator = RandomDataGenerator()
random_student_generator = generator.generate_data(structure, size=1000)

# 打印前五个生成的随机学生信息
for _ in range(5):
    print(next(random_student_generator))
