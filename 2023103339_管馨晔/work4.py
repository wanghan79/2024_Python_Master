import random
import string

class RandStructGen:
    def __init__(self):
        pass

    def rand_val(self):
        return random.choice([
            random.randint(1, 100),
            random.uniform(1.0, 100.0),
            ''.join(random.choices(string.ascii_letters + string.digits, k=5)),
            None,
            True,
            False
        ])

    def rand_struct(self, struct):
        if isinstance(struct, list):
            return [self.rand_struct(item) for item in struct]
        elif isinstance(struct, tuple):
            return tuple(self.rand_struct(item) for item in struct)
        elif isinstance(struct, dict):
            return {key: self.rand_struct(value) for key, value in struct.items()}
        else:
            return self.rand_val()

def generate_random_struct(struct):
    generator = RandStructGen()
    while True:
        yield generator.rand_struct(struct)

# 示例
example_struct = [
    {"x": [10, 20], "y": (30, 40)},
    (50, 60),
    [70, 80]
]

gen_instance = generate_random_struct(example_struct)
print(next(gen_instance))
print(next(gen_instance))
