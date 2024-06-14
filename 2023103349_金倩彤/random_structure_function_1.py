import random
import string

def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def random_integer(min_value=1, max_value=100):
    return random.randint(min_value, max_value)

def random_float(min_value=1.0, max_value=100.0):
    return random.uniform(min_value, max_value)

def random_phone_number():
    return '+86 ' + ''.join(random.choices(string.digits, k=11))

def generate_random_data(structure):
    if isinstance(structure, dict):
        result = {}
        for key, value in structure.items():
            if isinstance(value, dict) and 'type' in value:
                data_type = value['type']
                if data_type == 'string':
                    result[key] = random_string(**value.get('params', {}))
                elif data_type == 'integer':
                    result[key] = random_integer(**value.get('params', {}))
                elif data_type == 'float':
                    result[key] = random_float(**value.get('params', {}))
                elif data_type == 'phone':
                    result[key] = random_phone_number()
                else:
                    raise ValueError(f"Unsupported data type: {data_type}")
            else:
                raise ValueError("Invalid value specification")
        return result
    else:
        raise ValueError("Structure must be a dictionary")
    

# data_structure = {
#     'students': [
#         {
#             'name': {'type': 'string', 'params': {'length': 10}},
#             'id': {'type': 'integer', 'params': {'min_value': 1, 'max_value': 10000}},
#             'contact': {'type': 'phone'},
#             'age': {'type': 'integer', 'params': {'min_value': 18, 'max_value': 25}},
#             'gpa': {'type': 'float', 'params': {'min_value': 2.0, 'max_value': 4.0}},
#             'custom_field': {'type': 'str'} 
#         } for _ in range(10) 
#     ]
# }

# random_data =generate_random_data(data_structure)