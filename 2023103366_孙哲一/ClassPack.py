import random
import string
from typing import Any, List, Dict, Tuple

class Generator:
    def __init__(self, a: Any):
        self.a = a

    def generate(self) -> Any:
        return self._generate_random_structure(self.a)

    def _generate_random_structure(self, a: Any) -> Any:
        if isinstance(a, tuple) and len(a) == 2:
            if all(isinstance(i, int) for i in a):
                return random.randint(a[0], a[1])
            elif all(isinstance(i, float) for i in a):
                return round(random.uniform(a[0], a[1]), 1)
        elif isinstance(a, int):
            return random.randint(0, 100)
        elif isinstance(a, float):
            return round(random.uniform(170, 190), 1)
        elif isinstance(a, str):
            return ''.join(random.choices(string.ascii_letters, k=3))
        elif isinstance(a, list):
            return [self._generate_random_structure(item) for item in a]
        elif isinstance(a, dict):
            return {key: self._generate_random_structure(value) for key, value in a.items()}
        else:
            return None

a = {
    "name": "",
    "age": (18, 25),
    "height": (170.0, 190.0),
    "Parent": [
        {
            "name": "",
            "age": (40, 50)
        },
    ]
}
generator = Generator(a)
result = generator.generate()
print(result)
