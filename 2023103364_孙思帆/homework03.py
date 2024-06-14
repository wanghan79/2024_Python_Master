import random
import string
from functools import wraps
from types import SimpleNamespace

def randomize_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
   
        new_args = tuple(randomize_element(arg) for arg in args)
 
        new_kwargs = {key: randomize_element(value) for key, value in kwargs.items()}
        return func(*new_args, **new_kwargs)
    return wrapper

def randomize_element(element):
    if isinstance(element, list):
        return [randomize_element(x) for x in element]
    elif isinstance(element, tuple):
        return tuple(randomize_element(x) for x in element)
    elif isinstance(element, dict):
        return {key: randomize_element(value) for key, value in element.items()}
    elif isinstance(element, str):

        return ''.join(random.choices(string.ascii_letters + string.digits, k=len(element)))
    elif isinstance(element, int):
   
        return random.randint(0, 100)
    elif isinstance(element, float):

        return round(random.uniform(0, 100), 2)
    elif isinstance(element, SimpleNamespace):
      
        for attr in dir(element):
            if not attr.startswith('__'):
                setattr(element, attr, randomize_element(getattr(element, attr)))
        return element
    else:
      
        return element

@randomize_input
def my_function(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)


custom_obj = SimpleNamespace(attr1='value1', attr2=2)
my_function((1, 'a', 3.5), [21, [23, 556]], {'key1': 'value1', 'key2': 42}, custom_obj=custom_obj)
