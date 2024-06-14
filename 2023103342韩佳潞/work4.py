import random
import string

def create_string(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def create_int(max_value=100):
    return random.randint(1, max_value)

def create_list(element_type, length=5):
    if element_type == 'int':
        return [create_int() for _ in range(length)]
    elif element_type == 'string':
        return [create_string() for _ in range(length)]
    else:
        raise ValueError("不属于list")

def create_tuple(element_type, length=5):
    return tuple(create_list(element_type, length))

data_type = {
    'num_students': 3,
    'field_types': {
        'name': ('string', None, 10),
        'student_id': ('string', None, 10),
        'major': ('string', None, 8),
        'grades': ('list', 'int', 5),
        'research': ('tuple', 'string', 3)
    }
}

def generate_students(field_types, num_students):
    for _ in range(num_students):
        student_info = {}
        for field, (field_type, element_type, length) in field_types.items():
            if field_type == 'string':
                student_info[field] = create_string(length)
            elif field_type == 'int':
                student_info[field] = create_int()
            elif field_type == 'list':
                student_info[field] = create_list(element_type, length)
            elif field_type == 'tuple':
                student_info[field] = create_tuple(element_type, length)
            else:
                continue
        yield student_info

def main():
    student_generator = generate_students(data_type['field_types'], data_type['num_students'])
    
    for student in student_generator:
        for key, value in student.items():
            print(f"{key.capitalize()}: {value}")
        print()

main()
