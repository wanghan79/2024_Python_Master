
import random
def generate_random_numbers(**params):
    if 'type' in params and 'range' in params and 'size' in params:
        rand_type = params['type']
        rand_range = params['range']
        rand_size = params['size']

        if rand_type == 'int':
            rand_nums = [random.randint(rand_range[0], rand_range[1]) for _ in range(rand_size)]
        elif rand_type == 'float':
            rand_nums = [random.uniform(rand_range[0], rand_range[1]) for _ in range(rand_size)]
        else:
            raise ValueError("Unsupported random number type. Supported types: 'int', 'float'")

        return rand_nums
    else:
        raise ValueError("Missing required parameters. Required: 'type', 'range', 'size'")
    
params1 = {'type': 'int', 'range': (1, 100), 'size': 5}
params2 = {'type': 'float', 'range': (0.0, 1.0), 'size': 3}

random_integers = generate_random_numbers(**params1)
random_floats = generate_random_numbers(**params2)

print("随机整数:", random_integers)
print("随机浮点数:", random_floats)
