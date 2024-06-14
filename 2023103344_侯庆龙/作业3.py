import random
import string
from functools import wraps

def randomize_params(param_spec):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            randomized_kwargs = {param: generate_random_value(spec) for param, spec in param_spec.items()}
            return func(*args, **randomized_kwargs)
        return wrapper
    return decorator

def generate_random_value(spec):
    if spec['type'] == 'int':
        return random.randint(*spec['range'])
    elif spec['type'] == 'float':
        return round(random.uniform(*spec['range']), 2)
    elif spec['type'] == 'str':
        return ''.join(random.choices(string.ascii_letters + string.digits, k=spec['length']))
    elif spec['type'] == 'bool':
        return random.choice([True, False])
    elif spec['type'] == 'list':
        return [generate_random_value(spec['element']) for _ in range(random.randint(*spec['length']))]
    elif spec['type'] == 'tuple':
        return tuple(generate_random_value(spec['element']) for _ in range(random.randint(*spec['length'])))
    elif spec['type'] == 'dict':
        return {generate_random_value(spec['key']): generate_random_value(spec['value']) for _ in range(random.randint(*spec['length']))}
    else:
        return None

def randomize_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        randomized_args = [randomize_value(arg) for arg in args]
        randomized_kwargs = {key: randomize_value(value) for key, value in kwargs.items()}
        return func(*randomized_args, **randomized_kwargs)
    return wrapper

def randomize_value(value):
    if isinstance(value, (list, tuple)):
        return type(value)(randomize_value(item) for item in value)
    elif isinstance(value, dict):
        return {key: randomize_value(val) for key, val in value.items()}
    elif isinstance(value, str):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=len(value)))
    elif isinstance(value, int):
        return random.randint(0, 100)
    elif isinstance(value, float):
        return round(random.uniform(0, 100), 2)
    elif hasattr(value, '__dict__'):
        for attr in vars(value):
            setattr(value, attr, randomize_value(getattr(value, attr)))
        return value
    else:
        return value

# 测试函数
@randomize_params({
    'x': {'type': 'int', 'range': (0, 100)},
    'y': {'type': 'float', 'range': (0.0, 10.0)},
    'name': {'type': 'str', 'length': 5},
    'flag': {'type': 'bool'}
})
@randomize_input
def example_function(x=None, y=None, name=None, flag=None, *args, **kwargs):
    print("x:", x)
    print("y:", y)
    print("name:", name)
    print("flag:", flag)
    print("Args:", args)
    print("Kwargs:", kwargs)

# 测试
CustomObject = type('CustomObject', (), {'attr1': 'value1', 'attr2': 2})
custom_instance = CustomObject()
example_function((1, 'example', 3.5), [21, [23, 556]], {'key1': 'value1', 'key2': 42}, custom_obj=custom_instance)
