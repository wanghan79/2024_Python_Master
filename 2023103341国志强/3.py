import random
import string
from functools import wraps

def randomize_arguments(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        new_args = [randomize(arg) for arg in args]
        new_kwargs = {key: randomize(value) for key, value in kwargs.items()}
        return func(*new_args, **new_kwargs)
    return wrapper

def randomize(value):
    if isinstance(value, (list, tuple)):
        return type(value)(randomize(item) for item in value)
    elif isinstance(value, dict):
        return {key: randomize(val) for key, val in value.items()}
    elif isinstance(value, str):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=len(value)))
    elif isinstance(value, int):
        return random.randint(0, 100)
    elif isinstance(value, float):
        return round(random.uniform(0, 100), 2)  # Round to 2 decimal places for floats
    elif hasattr(value, '__dict__'):  # Check if it is an object with __dict__
        for attr in value.__dict__:
            setattr(value, attr, randomize(getattr(value, attr)))
        return value
    else:
        return value

@randomize_arguments
def process_data(*args, **kwargs):
    print("Arguments:", args)
    print("Keyword Arguments:", kwargs)


class CustomObject:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

process_data((1, 'a', 3.5), [21, [23, 556]], {'key1': 'value1', 'key2': 42}, custom_obj=CustomObject('value1', 2))
