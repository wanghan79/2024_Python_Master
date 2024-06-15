import random
import string

class RandomGen:
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

# 示例
gen = RandomGen()
input_struct = [1, "a", {"key": (2, 3)}, [4, 5]]
random_struct = gen.rand_struct(input_struct)
print(random_struct)
