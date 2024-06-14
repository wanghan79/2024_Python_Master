import random
import string


def generate_random_structure(*args, **kwargs):
    results = []
    for arg in args:
        if isinstance(arg, int):
            results.append(random.randint(0, arg))
        elif isinstance(arg, float):
            results.append(random.uniform(0, arg))
        elif isinstance(arg, str) and arg == 'string':
            results.append(''.join(random.choices(string.ascii_letters + string.digits, k=10)))
        elif isinstance(arg, list):
            results.append(random.choice(arg))

    for key, value in kwargs.items():
        if isinstance(value, int):
            results.append(random.randint(0, value))
        elif isinstance(value, float):
            results.append(random.uniform(0, value))
        elif isinstance(value, str) and value == 'string':
            results.append(''.join(random.choices(string.ascii_letters + string.digits, k=10)))
        elif isinstance(value, list):
            results.append(random.choice(value))

    return results


# 使用例子
if __name__ == "__main__":
    print(generate_random_structure(10, 5.5, 'string', [1, 2, 3, 4, 5], key1=100, key2=50.5, key3='string',
                                    key4=['a', 'b', 'c', 'd']))
