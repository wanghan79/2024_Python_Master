import random


def create_random_sequence(random_type, value_range, sequence_length):
    if random_type not in ['int', 'float']:
        raise ValueError("Unsupported random number type. Supported types: 'int', 'float'")

    if random_type == 'int':
        return [random.randint(value_range[0], value_range[1]) for _ in range(sequence_length)]
    elif random_type == 'float':
        return [random.uniform(value_range[0], value_range[1]) for _ in range(sequence_length)]


integer_params = {'random_type': 'int', 'value_range': (1, 100), 'sequence_length': 5}
float_params = {'random_type': 'float', 'value_range': (0.0, 1.0), 'sequence_length': 3}

integers = create_random_sequence(**integer_params)
floats = create_random_sequence(**float_params)

print("随机整数序列:", integers)
print("随机浮点数序列:", floats)
