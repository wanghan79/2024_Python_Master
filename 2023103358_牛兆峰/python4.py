import random
import string

def structDataSampling(**kwargs):

    for _ in range(kwargs['num']):
        result = {}
        for key, value in kwargs['struct'].items():
            if key == int:
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == float:
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == str:
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            result[key] = tmp
        yield result

def run():
 
    gen = structDataSampling(num=5, struct={int: {'datarange': (0, 10)},
                                            str: {'datarange': string.ascii_letters, 'len': 10},
                                            float: {'datarange': (0, 1.0)}})
    results = list(gen)
    print(results)

if __name__ == '__main__':
    run()
