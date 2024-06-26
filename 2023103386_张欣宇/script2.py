import random
class Factory:

    def __init__(self, *args):
        self.methods = args

    def generate_sampling(self):
        def data_sampling(**kwargs):
            result = []

            for key, value in kwargs.items():
                # print(key, value)
                if key == 'int':
                    result.append(random.randint(*value))
                elif key == 'float':
                    result.append(random.uniform(*value))
                elif key == 'str':
                    length = random.randint(*value)
                    result.append(''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=length)))
                elif key == 'list':
                    result.append([i for i in range(value[0][0], value[0][1])])

            return result

        for metric in ['ACC', 'MCC', 'F1', 'RECALL']:
            if metric in self.methods:
                print(f"{metric} accuracy is calculating...")

        for method in self.methods:
            print(f"{method} machine learning is Applying ...")

        return data_sampling


factory = Factory('SVM', 'RF', 'ACC', 'F1')

dataSampling = factory.generate_sampling()

data = dataSampling(int=(1, 100), float=(0.0, 1.0), str='mingtian')
print(data)
