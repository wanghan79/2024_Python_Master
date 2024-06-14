import random
import string

class DataSampler:
    def __init__(self, num, struct):
        self.num = num
        self.struct = struct

    def structDataSampling(self):
        results = list()
        for _ in range(self.num):
            result = list()
            for key, value in self.struct.items():
                if key is int:
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it), next(it))
                elif key is float:
                    it = iter(value['datarange'])
                    tmp = random.uniform(next(it), next(it))
                elif key is str:
                    tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
                else:
                    continue  # Skip unknown types
                result.append(tmp)
            results.append(result)
        return results

    def displaySamples(self):
        print("随机生成结构体")
        samples = self.structDataSampling()
        for sample in samples:
            print(sample)
        print("job1_yzy ^_^")

if __name__ == '__main__':
    sampler = DataSampler(num=5, struct={int: {'datarange': (0, 10)},
                                         str: {'datarange': string.ascii_letters + "&*_", 'len': 10},
                                         float: {'datarange': (0, 1.0)}})
    sampler.displaySamples()
