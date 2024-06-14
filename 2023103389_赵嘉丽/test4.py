import random
import string

class RandomDataGenerator:
    def __init__(self, num, **kwargs):
        self.num = num
        self.kwargs = kwargs

    def generate(self):
        for _ in range(self.num):
            element = []
            for key, value in self.kwargs.items():
                if key == "int":
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it), next(it))
                elif key == "float":
                    it = iter(value['datarange'])
                    tmp = random.uniform(next(it), next(it))
                elif key == "str":
                    tmp = ''.join(random.choice(value['datarange']) for _ in range(value['len']))
                element.append(tmp)
            yield element

def main():
    struct = {
        "num": 3,
        "int": {"datarange": [1, 100]},
        "float": {"datarange": [1.0, 100.0]},
        "str": {"datarange": string.ascii_letters, "len": 5}
    }
    generator = RandomDataGenerator(**struct)
    for sample in generator.generate():
        print(sample)

if __name__ == '__main__':
    main()
