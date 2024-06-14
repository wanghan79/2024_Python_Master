import random
import string
from functools import wraps

def random_structure_generator(*args):
    def decorator(func):
        @wraps(func)
        def wrapper(*func_args, **func_kwargs):
            def random_value():
                return random.choice([
                    random.randint(1, 100),  # 随机整数
                    random.uniform(1.0, 100.0),  # 随机浮点数
                    ''.join(random.choices(string.ascii_letters + string.digits, k=5)),  # 随机字符串
                    None,  # None值
                    True,  # 布尔值True
                    False  # 布尔值False
                ])

            def generate_random_structure(structure):
                if isinstance(structure, list):
                    return [generate_random_structure(item) for item in structure]
                elif isinstance(structure, tuple):
                    return tuple(generate_random_structure(item) for item in structure)
                elif isinstance(structure, dict):
                    return {key: generate_random_structure(value) for key, value in structure.items()}
                else:
                    return random_value()

            randomized_args = tuple(generate_random_structure(arg) for arg in args)
            return func(*randomized_args, *func_args, **func_kwargs)

        return wrapper

    return decorator

@random_structure_generator(
    [{"key1": [1, 2], "key2": (3, 4)}, (5, 6), [7, 8]]
)
def example_function(*args):
    return args


randomized_structure = example_function()
print(randomized_structure)
