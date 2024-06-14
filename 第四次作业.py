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
                    for item in structure:
                        yield from generate_random_structure(item)
                elif isinstance(structure, tuple):
                    for item in structure:
                        yield from generate_random_structure(item)
                elif isinstance(structure, dict):
                    for key, value in structure.items():
                        yield key, list(generate_random_structure(value))
                else:
                    yield random_value()

            def construct_structure(gen, template):
                if isinstance(template, list):
                    return [construct_structure(gen, item) for item in template]
                elif isinstance(template, tuple):
                    return tuple(construct_structure(gen, item) for item in template)
                elif isinstance(template, dict):
                    result = {}
                    for key in template:
                        value_gen = next(gen)
                        if isinstance(value_gen, tuple):
                            key, subgen = value_gen
                            result[key] = construct_structure(iter(subgen), template[key])
                        else:
                            result[key] = value_gen
                    return result
                else:
                    return next(gen)

            gen = generate_random_structure(args[0])
            randomized_structure = construct_structure(gen, args[0])
            return func(randomized_structure, *func_args, **func_kwargs)

        return wrapper

    return decorator

@random_structure_generator(
    [{"key1": [1, 2], "key2": (3, 4)}, (5, 6), [7, 8]]
)
def example_function(random_structure):
    return random_structure


randomized_structure = example_function()
print(randomized_structure)