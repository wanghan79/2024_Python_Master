import random

def generate_random_value(data_type, **kwargs):
    """生成基于数据类型和附加关键字参数的随机值。"""
    if data_type == int:
        return random.randint(kwargs.get('int_min', 1), kwargs.get('int_max', 100))
    elif data_type == float:
        return random.uniform(kwargs.get('float_min', 1.0), kwargs.get('float_max', 100.0))
    elif data_type == str:
        length = kwargs.get('str_len', 10)
        chars = kwargs.get('str_chars', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        return ''.join(random.choices(chars, k=length))
    elif data_type == list:
        # 如果是列表，生成列表中的每个元素
        element_types = kwargs.get('list_elements', [int])
        return [generate_random_value(t, **kwargs) for t in element_types]
    elif data_type == dict:
        # 如果是字典，生成字典中的每个值
        keys = kwargs.get('dict_keys', {})
        return {k: generate_random_value(v, **kwargs) for k, v in keys.items()}
    else:
        raise ValueError(f"Unsupported type {data_type}")

def generate_data_from_structure(structure, **kwargs):
    if isinstance(structure, dict):
        return {key: generate_data_from_structure(value, **kwargs) for key, value in structure.items()}
    elif isinstance(structure, list):
        return [generate_data_from_structure(item, **kwargs) for item in structure]
    elif isinstance(structure, type):
        return generate_random_value(structure, **kwargs)
    else:
        return structure

# 定义期望的数据结构
data_structure = {
    'int_value': int,
    'str_value': str,
    'complex_list': {'type': list, 'list_elements': [int, str, float]},
    'complex_dict': {
        'type': dict,
        'dict_keys': {
            'nested_int': int,
            'nested_str': str,
            'nested_list': {'type': list, 'list_elements': [float, {'type': str, 'str_len': 20}]}
        }
    }
}

if __name__ == '__main__':
    # 传递额外参数以控制随机值生成
    random_data = generate_data_from_structure(data_structure, int_min=10, int_max=500, float_min=0.1, float_max=50.0, str_len=12)
    print(random_data)
