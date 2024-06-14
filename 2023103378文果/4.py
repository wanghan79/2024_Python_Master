import random
import string
from functools import wraps

def random_value():
    """
    生成一个随机值，可以是整数、浮点数、字符串、None、True或False。
    """
    return random.choice([
        random.randint(1, 100),
        random.uniform(1.0, 100.0),
        ''.join(random.choices(string.ascii_letters + string.digits, k=5)),
        None,
        True,
        False
    ])

def generate_random_structure(template):
   
    if isinstance(template, list):
        return [generate_random_structure(item) for item in template]
    elif isinstance(template, tuple):
        return tuple(generate_random_structure(list(item)) for item in template)
    elif isinstance(template, dict):
        return {key: generate_random_structure(value) for key, value in template.items()}
    else:
        return random_value()

def random_structure_decorator(template):
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            randomized_structure = generate_random_structure(template)
            return func(randomized_structure, *args, **kwargs)
        return wrapper
    return decorator

@random_structure_decorator([{"key1": [1, 2], "key2": (3, 4)}, (5, 6), [7, 8]])
def example_function(random_structures, *args, **kwargs):
   
    print("Randomized Structure:")
    print(random_structures)

if __name__ == '__main__':
    example_function()
