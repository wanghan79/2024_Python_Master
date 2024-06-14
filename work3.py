import random
import string
from functools import wraps

class Randomizer:
    def __init__(self, int_range=(0, 100), float_range=(0.0, 100.0), str_len=8):
        self.int_range = int_range
        self.float_range = float_range
        self.str_len = str_len
    
    def randomize_element(self, element):
        if isinstance(element, (list, tuple)):
            return type(element)(self.randomize_element(x) for x in element)
        elif isinstance(element, dict):
            return {key: self.randomize_element(value) for key, value in element.items()}
        elif isinstance(element, str):
            return ''.join(random.choices(string.ascii_letters + string.digits, k=self.str_len))
        elif isinstance(element, int):
            return random.randint(*self.int_range)
        elif isinstance(element, float):
            return random.uniform(*self.float_range)
        elif hasattr(element, '__dict__'):
            for attr in vars(element):
                setattr(element, attr, self.randomize_element(getattr(element, attr)))
            return element
        else:
            return element

    def randomize_input(self, int_range=None, float_range=None, str_len=None):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                if int_range:
                    self.int_range = int_range
                if float_range:
                    self.float_range = float_range
                if str_len:
                    self.str_len = str_len
                new_args = [self.randomize_element(arg) for arg in args]
                new_kwargs = {key: self.randomize_element(value) for key, value in kwargs.items()}
                return func(*new_args, **new_kwargs)
            return wrapper
        return decorator

# 测试
randomizer = Randomizer()

@randomizer.randomize_input(int_range=(10, 50), float_range=(10.0, 50.0), str_len=5)
def my_function(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

my_function((1, 'a', 3.5), {'key1': 'value1', 'key2': 42}, custom_obj=type('Custom', (), {'attr1': 'value1', 'attr2': 2})())
