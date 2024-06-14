import random
import string
from typing import Any, Generator

class Generator:
    def __init__(self, a: Any):
        self.a = a

    def generate_iter(self) -> Generator[Any, None, None]:
        yield from self._generate_random_structure_iter(self.a)

    def _generate_random_structure_iter(self, a: Any) -> Generator[Any, None, None]:
        if isinstance(a, tuple) and len(a) == 2:
            if all(isinstance(i, int) for i in a):
                yield random.randint(a[0], a[1])
            elif all(isinstance(i, float) for i in a):
                yield round(random.uniform(a[0], a[1]), 1)
        elif isinstance(a, int):
            yield random.randint(0, 100)
        elif isinstance(a, float):
            yield round(random.uniform(170, 190), 1)
        elif isinstance(a, str):
            yield ''.join(random.choices(string.ascii_letters, k=3))
        elif isinstance(a, list):
            result = []
            for item in a:
                result.append(next(self._generate_random_structure_iter(item)))
            yield result
        elif isinstance(a, dict):
            result = {}
            for key, value in a.items():
                result[key] = next(self._generate_random_structure_iter(value))
            yield result
        else:
            yield None

a = {
    "name": "",
    "age": (18, 25),
    "height": (170.0, 190.0),
    "Parent": [
        {
            "name": "",
            "age": (40, 50)
        }
    ]
}
generator = Generator(a)
for part in generator.generate_iter():
    print(part)
