import random
import string


def random_structure_generator(*args, **kwargs):
    for arg in args:
        if isinstance(arg, int):
            yield random.randint(0, arg)
        elif isinstance(arg, float):
            yield random.uniform(0, arg)
        elif isinstance(arg, str) and arg == 'string':
            yield ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        elif isinstance(arg, list):
            yield random.choice(arg)

    for key, value in kwargs.items():
        if isinstance(value, int):
            yield random.randint(0, value)
        elif isinstance(value, float):
            yield random.uniform(0, value)
        elif isinstance(value, str) and value == 'string':
            yield ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        elif isinstance(value, list):
            yield random.choice(value)


# 使用例子
if __name__ == "__main__":
    generator = random_structure_generator(10, 5.5, 'string', [1, 2, 3, 4, 5], key1=100, key2=50.5, key3='string',
                                           key4=['a', 'b', 'c', 'd'])
    for value in generator:
        print(value)
