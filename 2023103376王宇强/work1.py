import random

def randomize_element(element, int_range=(0, 100), float_range=(0.0, 100.0), str_len=8):
    if isinstance(element, (list, tuple)):
        return type(element)(randomize_element(x, int_range, float_range, str_len) for x in element)
    elif isinstance(element, dict):
        return {key: randomize_element(value, int_range, float_range, str_len) for key, value in element.items()}
    elif isinstance(element, str):
        return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=str_len))
    elif isinstance(element, int):
        return random.randint(*int_range)
    elif isinstance(element, float):
        return random.uniform(*float_range)
    elif hasattr(element, '__dict__'):
        for attr in vars(element):
            setattr(element, attr, randomize_element(getattr(element, attr), int_range, float_range, str_len))
        return element
    else:
        return element

def randomize_input(*args, **kwargs):
    return [randomize_element(arg) for arg in args], {key: randomize_element(value) for key, value in kwargs.items()}

# 测试
print(randomize_input((1, 'a', 3.5), {'key1': 'value1', 'key2': 42}, custom_obj=type('Custom', (), {'attr1': 'value1', 'attr2': 2})()))
